import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(multiply_int(5, 0), 0)

    def test_one(self):
        self.assertEqual(multiply_int(5, 1), 5)

    def test_positive(self):
        self.assertEqual(multiply_int(5, 2), 10)

    def test_negative(self):
        self.assertEqual(multiply_int(5, -2), -10)

    def test_negative_zero(self):
        self.assertEqual(multiply_int(5, -0), 0)

    def test_edge_case(self):
        self.assertEqual(multiply_int(-5, 0), 0)

    def test_edge_case2(self):
        self.assertEqual(multiply_int(0, 0), 0)

    def test_edge_case3(self):
        self.assertEqual(multiply_int(0, 1), 0)

    def test_edge_case4(self):
        self.assertEqual(multiply_int(5, 1e10), 5e10)

    def test_edge_case5(self):
        self.assertEqual(multiply_int(-5, 1e10), -5e10)
