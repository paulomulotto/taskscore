import pytest
from taskscore.optimizer import calculate_task_score


class TestCalculateTaskScore:
    """
    Test class for calculating task scores.
    """

    def test_minimum_values(self):
        """
        Test case for calculating task score with minimum values.
        """
        assert calculate_task_score(1, 1) == 25.0

    def test_maximum_values(self):
        """
        Test case for calculating task score with maximum values.
        """
        assert calculate_task_score(4, 4) == 25.0

    def test_exception_values(self):
        """
        Test case for handling exception values.
        """
        with pytest.raises(ValueError):
            calculate_task_score(0, 1)
        with pytest.raises(ValueError):
            calculate_task_score(1, 0)
        with pytest.raises(ValueError):
            calculate_task_score(5, 1)
        with pytest.raises(ValueError):
            calculate_task_score(1, 5)
