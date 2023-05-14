import os
import torch
import torch.distributed.rpc as rpc
import torch.optim as optim
from torch.distributed.rpc import RRef

# Define a simple linear model.
class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

def run_worker(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '29500'
    rpc.init_rpc("worker{}".format(rank), rank=rank, world_size=world_size)

    if rank == 0:
        # Rank 0 is the master.
        # Create an RRef to the model on the worker.
        model_rref = rpc.remote("worker1", LinearModel)

        # Define a loss function and an optimizer.
        loss_fn = torch.nn.MSELoss()
        opt = optim.SGD(model_rref.parameters(), lr=0.01)

        # Train the model.
        for _ in range(100):
            # Generate input and target data.
            x = torch.randn(1)
            y = 2 * x + 1

            with torch.distributed.autograd.context() as context_id:
                y_pred = rpc.rpc_sync(model_rref.owner(), model_rref.to_here, args=(x,))
                loss = loss_fn(y_pred, y)
                torch.distributed.autograd.backward(context_id, [loss])

                # Perform an optimizer step using RPC.
                rpc.rpc_sync(
                    model_rref.owner(),
                    torch.distributed.optim.Optimizer.step,
                    args=(RRef(opt), context_id)
                )

        print("Model training complete.")
    else:
        # Worker 1 holds the model.
        pass

    # Shutdown RPC for all workers.
    rpc.shutdown()

if __name__ == "__main__":
    world_size = 2
    for rank in range(world_size):
        run_worker(rank, world_size)
