import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))
        self.assertTrue(check([-1, -2, -3, -4, -5], 5))
        self.assertTrue(check([0, 1, 2, 3, 4], 5))

    def test_edge_case_1(self):
        self.assertFalse(check([1, 0, 1], 3))
        self.assertFalse(check([-1, 0, -1], 3))

    def test_edge_case_2(self):
        self.assertTrue(check([1, 1], 2))
        self.assertTrue(check([-1, -1], 2))

    def test_corner_case_1(self):
        self.assertFalse(check([1, 1, 1], 3))
        self.assertFalse(check([-1, -1, -1], 3))

    def test_corner_case_2(self):
        self.assertTrue(check([1, 0, 1], 3))
        self.assertTrue(check([-1, 0, -1], 3))
