import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):
    def test_consecutive_list(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_consecutive_empty_list(self):
        self.assertTrue(check_Consecutive([]))

    def test_consecutive_single_element(self):
        self.assertTrue(check_Consecutive([1]))

    def test_consecutive_decreasing_list(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1]))

    def test_consecutive_increasing_with_gap_list(self):
        self.assertFalse(check_Consecutive([1, 3, 5]))

    def test_consecutive_list_with_min_max_boundary(self):
        self.assertTrue(check_Consecutive([0, 1, 2, 3, 4]))

    def test_consecutive_list_with_min_max_boundary_negative(self):
        self.assertTrue(check_Consecutive([-1, -2, -3, -4, -5]))

    def test_consecutive_list_with_duplicates(self):
        self.assertTrue(check_Consecutive([1, 1, 2, 3]))

    def test_consecutive_list_with_non_consecutive_elements(self):
        self.assertFalse(check_Consecutive([1, 3, 4, 5]))

    def test_consecutive_list_with_non_integer_elements(self):
        self.assertRaises(TypeError, check_Consecutive, [1.1, 2.2, 3.3])
