import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(6), 6)
        self.assertEqual(sum_div(12), 15)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_div(0), 0)
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 1)

    def test_corner_cases(self):
        self.assertEqual(sum_div(100), 111)
        self.assertEqual(sum_div(220), 284)
