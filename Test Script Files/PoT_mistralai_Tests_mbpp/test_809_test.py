import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):
    def test_typical_cases(self):
        self.assertFalse(check_smaller((1, 2, 3), (2, 1, 3)))
        self.assertTrue(check_smaller((1, 2, 3), (1, 2, 4)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 3, 2)))
        self.assertFalse(check_smaller((1, 2, 3), (3, 2, 1)))

    def test_edge_and_boundary_cases(self):
        self.assertTrue(check_smaller((0, 0, 0), (0, 0, 0)))
        self.assertTrue(check_smaller((-1, -2, -3), (-2, -1, -3)))
        self.assertFalse(check_smaller((-1, -2, -3), (-3, -2, -1)))
        self.assertTrue(check_smaller((1e100, 1, 0), (1e100, 1, 1)))
        self.assertFalse(check_smaller((1e100, 1, 0), (1e100, 1, 2)))
