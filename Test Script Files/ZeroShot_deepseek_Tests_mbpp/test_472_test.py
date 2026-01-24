import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_consecutive_numbers(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))
        self.assertTrue(check_Consecutive([10, 11, 12]))
        self.assertTrue(check_Consecutive([-1, 0, 1, 2, 3]))
        self.assertTrue(check_Consecutive([1]))
        self.assertTrue(check_Consecutive([]))

    def test_non_consecutive_numbers(self):
        self.assertFalse(check_Consecutive([1, 2, 4, 5]))
        self.assertFalse(check_Consecutive([10, 12, 14]))
        self.assertFalse(check_Consecutive([-1, 1, 2, 3]))
        self.assertFalse(check_Consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))

    def test_with_duplicates(self):
        self.assertFalse(check_Consecutive([1, 2, 2, 3, 4]))
        self.assertFalse(check_Consecutive([1, 1, 2, 3, 4]))
        self.assertFalse(check_Consecutive([1, 2, 3, 4, 4]))
