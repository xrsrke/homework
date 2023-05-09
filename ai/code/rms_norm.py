import torch
from torch import nn

# write RMS Norm in pytorch
class RMSNorm(nn.Module):
    def __init__(self, dim):
        super(RMSNorm, self).__init__()
        self.dim = dim

    def forward(self, x):
        return x / torch.sqrt(torch.mean(x**2, dim=self.dim, keepdim=True) + 1e-8)