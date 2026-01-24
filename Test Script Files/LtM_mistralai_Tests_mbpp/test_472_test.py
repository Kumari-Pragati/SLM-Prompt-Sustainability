import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(check_Consecutive([1, 2, 3]))
        self.assertTrue(check_Consecutive([5, 6, 7, 8, 9]))

    def test_edge_and_boundary(self):
        self.assertTrue(check_Consecutive([0, 1, 2]))
        self.assertTrue(check_Consecutive([10, 11, 12]))
        self.assertFalse(check_Consecutive([-1, 0, 1]))
        self.assertFalse(check_Consecutive([1, 2, 3, 4]))

    def test_complex(self):
        self.assertTrue(check_Consecutive([0, 1, 2, 3, 4, 5]))
        self.assertFalse(check_Consecutive([1, 3, 5, 7]))  # Odd numbers
        self.assertFalse(check_Consecutive([2, 4, 6, 8, 10, 12, 14]))  # Even numbers
        self.assertFalse(check_Consecutive([1, 3, 5, 7, 9, 11]))  # Odd numbers with a missing number
        self.assertFalse(check_Consecutive([2, 4, 6, 8, 10, 12, 14, 16]))  # Even numbers with a missing number
        self.assertFalse(check_Consecutive([1, 3, 5, 7, 9, 11, 13, 15, 17]))  # Odd numbers with a duplicate
        self.assertFalse(check_Consecutive([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))  # Even numbers with a duplicate
