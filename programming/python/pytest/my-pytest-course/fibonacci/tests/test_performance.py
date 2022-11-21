import pytest

from fibonacci.dynamic import fibonacci_dynamic_v2
from fibonacci.conftest import track_performance


@pytest.mark.performance
@track_performance
def test_performance():
    fibonacci_dynamic_v2(1000)
