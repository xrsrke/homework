# AUTOGENERATED! DO NOT EDIT! File to edit: ../02_test_fn.ipynb.

# %% auto 0
__all__ = ['a', 'b', 'test_func_1', 'test_func_2', 'test_func_3', 'test_func_4']

# %% ../02_test_fn.ipynb 3
import pytest

# %% ../02_test_fn.ipynb 4
def test_func_1():
    pass

# %% ../02_test_fn.ipynb 7
@pytest.mark.skip
def test_func_2():
    assert 1 == 2

# %% ../02_test_fn.ipynb 9
a, b = 3, 33

# %% ../02_test_fn.ipynb 12
@pytest.mark.xfail
def test_func_3():
    assert 1 == 2

# %% ../02_test_fn.ipynb 13
def test_func_4():
    pass