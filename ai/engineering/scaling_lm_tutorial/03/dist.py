import torch
import torch.distributed as dist
import os


# print(torch.backends.mps.is_built())

# os.environ["RANK"] = "0"
# os.environ["LOCAL_RANK"] = "0"
# os.environ["WORLD_SIZE"] = "1"

# os.environ["MASTER_ADDR"] = "localhost"
# os.environ["MASTER_PORT"] = "29500"

# dist.init_process_group(backend="nccl", rank=0, world_size=1)

# process_group = dist.new_group([0])

# print(process_group)

dist.init_process_group("nccl")
rank = dist.get_rank()
torch.cuda.set_device(rank)

if rank == 0:
    tensor = torch.randn(2, 2).to(torch.cuda.current_device())
else:
    tensor = torch.zeros(2, 2).to(torch.cuda.current_device())

print(f"before rank {rank} tensor {tensor}")
dist.broadcast(tensor, src=0)
print(f"after rank {rank} tensor {tensor}")
