import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):
    def test_consecutive_normal(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))
        self.assertTrue(check_Consecutive([-5, -4, -3, -2, -1]))
        self.assertTrue(check_Consecutive([10, 11, 12, 13, 14]))

    def test_consecutive_edge_cases(self):
        self.assertTrue(check_Consecutive([0, 1]))
        self.assertTrue(check_Consecutive([-1, -2, -3]))
        self.assertTrue(check_Consecutive([1, 2, 3, 4]))
        self.assertTrue(check_Consecutive([-5, -4, -3, -2]))
        self.assertTrue(check_Consecutive([10, 11, 12]))
        self.assertTrue(check_Consecutive([-10, -9, -8]))

    def test_consecutive_boundary(self):
        self.assertFalse(check_Consecutive([1, 2, 3, 5]))
        self.assertFalse(check_Consecutive([-5, -4, -3, -1]))
        self.assertFalse(check_Consecutive([1, 2, 3, 4, 6]))
        self.assertFalse(check_Consecutive([-5, -4, -3, -2, 0]))
        self.assertFalse(check_Consecutive([10, 11, 12, 14]))
        self.assertFalse(check_Consecutive([-10, -9, -8, -6]))

    def test_consecutive_invalid(self):
        self.assertFalse(check_Consecutive([1, 2, 3, 4, 5, 7]))
        self.assertFalse(check_Consecutive([-5, -4, -3, -2, 0, 1]))
        self.assertFalse(check_Consecutive([1, 2, 3, 4, 6, 8]))
        self.assertFalse(check_Consecutive([-5, -4, -3, -2, 0, -1]))
        self.assertFalse(check_Consecutive([10, 11, 12, 14, 16]))
        self.assertFalse(check_Consecutive([-10, -9, -8, -6, -4]))
