import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_consecutive_positive(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))
        self.assertTrue(check_Consecutive([-5, -4, -3, -2, -1]))
        self.assertTrue(check_Consecutive([0, 1, 2, 3, 4]))

    def test_consecutive_empty(self):
        self.assertFalse(check_Consecutive([]))

    def test_consecutive_single_element(self):
        self.assertFalse(check_Consecutive([1]))
        self.assertTrue(check_Consecutive([0]))

    def test_consecutive_duplicates(self):
        self.assertTrue(check_Consecutive([1, 1, 2, 3, 4]))
        self.assertTrue(check_Consecutive([1, 1, 1, 2, 3]))

    def test_consecutive_out_of_order(self):
        self.assertFalse(check_Consecutive([1, 3, 2]))
        self.assertFalse(check_Consecutive([-5, -3, -4]))

    def test_consecutive_gaps(self):
        self.assertFalse(check_Consecutive([1, 3, 4, 5]))
        self.assertFalse(check_Consecutive([-5, -4, 0, 2]))

    def test_consecutive_negative_range(self):
        self.assertTrue(check_Consecutive([-5, -4, -3, -2, -1]))

    def test_consecutive_large_range(self):
        self.assertTrue(check_Consecutive(list(range(-100, 101))))
