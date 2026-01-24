import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_gp(10, 3, 2), 32.0)
        self.assertEqual(sum_gp(5, 5, 3), 6.666666666666667)

    def test_edge_input(self):
        self.assertEqual(sum_gp(0, 3, 2), 0)
        self.assertEqual(sum_gp(1, 0, 2), math.nan)
        self.assertEqual(sum_gp(1, 1, 1), 1)
        self.assertEqual(sum_gp(1, 1, 0), math.nan)

    def test_complex_input(self):
        self.assertEqual(sum_gp(-10, 3, 2), -32.0)
        self.assertEqual(sum_gp(10, -3, 2), -32.0)
        self.assertEqual(sum_gp(10, 3, -2), -32.0)
        self.assertEqual(sum_gp(10, 3, 1.1), 29.545454545454547)
