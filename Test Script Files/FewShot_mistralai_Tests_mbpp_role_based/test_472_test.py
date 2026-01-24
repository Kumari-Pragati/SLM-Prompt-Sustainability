import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):
    def test_consecutive_ascending(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_consecutive_descending(self):
        self.assertTrue(check_Consecutive([5, 4, 3, 2, 1]))

    def test_consecutive_single_element(self):
        self.assertTrue(check_Consecutive([1]))

    def test_consecutive_empty_list(self):
        self.assertFalse(check_Consecutive([]))

    def test_consecutive_duplicates(self):
        self.assertTrue(check_Consecutive([1, 1, 2, 3]))

    def test_consecutive_negative_numbers(self):
        self.assertTrue(check_Consecutive([-5, -4, -3, -2, -1]))

    def test_consecutive_out_of_order(self):
        self.assertFalse(check_Consecutive([1, 3, 2]))

    def test_consecutive_negative_and_positive(self):
        self.assertFalse(check_Consecutive([-5, 1, 2, 3]))
