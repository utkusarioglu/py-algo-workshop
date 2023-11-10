import pytest
from climbing_stairs import climbingStairs

TEST_CASES = [
    {"params": 0, "expected": 0},
    {"params": 1, "expected": 1},
    {"params": 2, "expected": 2},
    {"params": 3, "expected": 3},
    {"params": 4, "expected": 5},
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_count(test_case):
    response = climbingStairs(test_case["params"])
    assert response == test_case["expected"]
