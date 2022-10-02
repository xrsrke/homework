# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/06_tests.test_companies.ipynb.

# %% auto 0
__all__ = ['a', 'b', 'logger', 'Company', 'TestGetCompanies', 'TestFeature', 'raise_exception',
           'test_raise_exception_should_pass', 'function_that_logs_something', 'test_logged_warning_level']

# %% ../../nbs/06_tests.test_companies.ipynb 4
import pytest
from unittest import TestCase

# %% ../../nbs/06_tests.test_companies.ipynb 5
class Company:
    def get(self):
        return []
    
    def list(self):
        return 1

# %% ../../nbs/06_tests.test_companies.ipynb 6
class TestGetCompanies(TestCase):
    def test_zero_companies_should_return_empty_list(self) -> None:
        self.assertEqual(Company().get(), [])
    
    def test_list_companies_should(self) -> None:
        self.assertIn(Company().list(), [4, 2])

# %% ../../nbs/06_tests.test_companies.ipynb 7
class Company:
    def list_companies(self):
        return 1

# %% ../../nbs/06_tests.test_companies.ipynb 11
class TestGetCompanies(TestCase):
    
    @pytest.mark.xfail
    def test_list_companies_should_return_one(self):
        list_companies = [1, 2, 3, 4]
        self.assertIn(Company().list_companies(), list_companies)
        self.assertEqual(1, 2)

# %% ../../nbs/06_tests.test_companies.ipynb 13
class TestFeature(TestCase):
    
    @pytest.mark.xfail
    def test_feature_one(self):
        self.assertEqual(1, 2)

# %% ../../nbs/06_tests.test_companies.ipynb 14
a, b = 4, 3

# %% ../../nbs/06_tests.test_companies.ipynb 16
class TestFeature(TestCase):
    
    # @pytest.mark.xfail
    @pytest.mark.skip
    def test_equal_should_return_true(self):
        self.assertEqual(a, b)

# %% ../../nbs/06_tests.test_companies.ipynb 17
def raise_exception():
    raise ValueError("This is a value error")

# %% ../../nbs/06_tests.test_companies.ipynb 19
def test_raise_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_exception()

# %% ../../nbs/06_tests.test_companies.ipynb 20
import logging

# %% ../../nbs/06_tests.test_companies.ipynb 21
logger = logging.getLogger("MY_LOG")

# %% ../../nbs/06_tests.test_companies.ipynb 22
def function_that_logs_something():
    logger.warning(f"logged message")

# %% ../../nbs/06_tests.test_companies.ipynb 24
def test_logged_warning_level(caplog):
    
    # code
    function_that_logs_something()
    assert "logged message" in caplog.text
