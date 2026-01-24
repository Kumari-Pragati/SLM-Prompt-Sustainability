import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))
        self.assertTrue(check([-1, -2, -3, -4, -5], 5))

    def test_edge_case_1(self):
        self.assertTrue(check([0, 1, 2, 3, 4], 5))
        self.assertTrue(check([-0, -1, -2, -3, -4], 5))

    def test_edge_case_2(self):
        self.assertTrue(check([1, 0, 2, 3, 4], 5))
        self.assertTrue(check([1, -0, 2, 3, 4], 5))

    def test_edge_case_3(self):
        self.assertTrue(check([1, 2, 3, 0, 4], 5))
        self.assertTrue(check([1, 2, 3, -0, 4], 5))

    def test_edge_case_4(self):
        self.assertTrue(check([1, 2, 3, 4, 0], 5))
        self.assertTrue(check([1, 2, 3, 4, -0], 5))

    def test_edge_case_5(self):
        self.assertTrue(check([1, 2, 3, 4, 0, 5], 6))
        self.assertTrue(check([1, 2, 3, 4, -0, 5], 6))

    def test_invalid_input_length(self):
        self.assertRaises(IndexError, check, [1, 2, 3], 4)
        self.assertRaises(IndexError, check, [1, 2, 3], -1)
