# import os
# import torch
# import torch.distributed as dist
# import torch.multiprocessing as mp

# def all_gather_example(rank, world_size):
#     """A simple example using torch.distributed.all_gather."""
#     # Initialize the process group
#     os.environ['MASTER_ADDR'] = 'localhost'
#     os.environ['MASTER_PORT'] = '12345'
#     dist.init_process_group("gloo", rank=rank, world_size=world_size)

#     # Create a tensor for the current rank
#     tensor = torch.tensor([rank]).float()
#     gathered_tensors = [torch.zeros(1) for _ in range(world_size)]
#     print(f"Before all_gather: Rank {rank}, tensor: {tensor}")
#     print(f"gathered_tensors: {gathered_tensors}")

#     # Perform all_gather operation
#     dist.all_gather(gathered_tensors, tensor)
#     print(f"After all_gather: Rank {rank}, gathered_tensors: {gathered_tensors}")

#     # Clean up
#     dist.destroy_process_group()

# def main():
#     world_size = 4
#     mp.spawn(all_gather_example, args=(world_size,), nprocs=world_size, join=True)

# if __name__ == "__main__":
#     main()


import torch
import torch.distributed as dist
import os

def init_distributed():
    # Replace these values with the actual values for your setup
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '29500'
    dist.init_process_group(backend='nccl', rank=2, world_size=2)

def gather_all_tensors(_, tensor):
    world_size = dist.get_world_size()
    rank = dist.get_rank()

    # Create a list to store the gathered tensors
    gathered_tensors = [torch.zeros_like(tensor) for _ in range(world_size)]

    # Perform the all_gather operation
    dist.all_gather(gathered_tensors, tensor)

    return gathered_tensors

if __name__ == "__main__":
    # Initialize the distributed environment
    init_distributed()

    tensor = torch.tensor([dist.get_rank()]).float()
    print(f"Before gather_all_tensors: Rank {dist.get_rank()}, tensor: {tensor}")

    gathered_tensors = gather_all_tensors(tensor)
    print(f"After gather_all_tensors: Rank {dist.get_rank()}, gathered_tensors: {gathered_tensors}")

