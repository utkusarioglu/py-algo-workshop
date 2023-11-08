import pytest
from container_with_most_water import ContainerWithMostWater

TEST_CASES = [
    {"params": [1, 8, 6, 2, 5, 4, 8, 3, 7], "expected": 49},
    {"params": [10, 10, 1, 1, 1], "expected": 10},
    {"params": [11, 10, 1, 1, 1], "expected": 10},
    {"params": [10, 11, 1, 1, 1], "expected": 10},
    {"params": [1, 1, 1, 10, 10], "expected": 10},
    {"params": [1, 1, 1, 10, 11], "expected": 10},
    {"params": [1, 1, 1, 11, 10], "expected": 10},
    {"params": [1, 1, 1, 1, 10], "expected": 4},
    {"params": [1, 2, 3, 4, 5], "expected": 6},
    {"params": [5, 4, 3, 2, 1], "expected": 6},
]


@pytest.fixture
def instance():
    yield ContainerWithMostWater()


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_find(instance, test_case):
    response = instance.greedy(test_case["params"])
    assert response == test_case["expected"]
