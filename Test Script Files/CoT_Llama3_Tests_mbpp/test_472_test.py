import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_consecutive_numbers(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_consecutive_numbers_with_duplicates(self):
        self.assertTrue(check_Consecutive([1, 2, 2, 3, 4, 5]))

    def test_consecutive_numbers_with_gaps(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 5, 6]))

    def test_consecutive_numbers_with_negative_numbers(self):
        self.assertTrue(check_Consecutive([-5, -4, -3, -2, -1]))

    def test_consecutive_numbers_with_positive_and_negative_numbers(self):
        self.assertTrue(check_Consecutive([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))

    def test_non_consecutive_numbers(self):
        self.assertFalse(check_Consecutive([1, 2, 4, 5]))

    def test_non_consecutive_numbers_with_duplicates(self):
        self.assertFalse(check_Consecutive([1, 2, 2, 3, 4, 5, 6]))

    def test_empty_list(self):
        self.assertFalse(check_Consecutive([]))

    def test_single_element_list(self):
        self.assertFalse(check_Consecutive([1]))

    def test_single_element_list_with_duplicates(self):
        self.assertFalse(check_Consecutive([1, 1]))

    def test_single_element_list_with_duplicates_and_gaps(self):
        self.assertFalse(check_Consecutive([1, 2, 3, 5, 6]))
