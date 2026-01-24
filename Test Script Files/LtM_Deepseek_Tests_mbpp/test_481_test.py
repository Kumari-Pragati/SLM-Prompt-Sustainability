import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9))
        self.assertFalse(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 30))

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertTrue(is_subset_sum([], 0, 0))
        self.assertFalse(is_subset_sum([1], 1, 0))
        self.assertTrue(is_subset_sum([1], 1, 1))
        self.assertFalse(is_subset_sum([1], 1, 2))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertTrue(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 30))
        self.assertFalse(is_subset_sum([3, 34, 4, 12, 5, 2], 6, 40))
