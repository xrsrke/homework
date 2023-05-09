import torch
import torch.utils.benchmark as benchmark


def add(x, y):
    return x + y


if __name__ == "__main__":
    x = torch.randn(10000, 64)
    t = benchmark.Timer(
        stmt="add(x, x)",
        setup="from __main__ import add"
    )
    t.timeit(10)
