import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_div(4), 3)
        self.assertEqual(sum_div(6), 3)
        self.assertEqual(sum_div(28), 14)

    def test_edge_input(self):
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 1)
        self.assertEqual(sum_div(3), 3)

    def test_boundary_input(self):
        self.assertEqual(sum_div(0), 0)
        self.assertEqual(sum_div(1000000), 2499985)

    def test_complex_input(self):
        self.assertEqual(sum_div(12), 6)
        self.assertEqual(sum_div(20), 10)
        self.assertEqual(sum_div(220), 110)
