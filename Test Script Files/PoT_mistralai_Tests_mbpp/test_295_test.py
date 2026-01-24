import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(sum_div(6), 3)
        self.assertEqual(sum_div(28), 14)
        self.assertEqual(sum_div(496), 712)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 2)
        self.assertEqual(sum_div(3), 3)
        self.assertEqual(sum_div(4), 2)
        self.assertEqual(sum_div(5), 4)
        self.assertEqual(sum_div(10), 4)
        self.assertEqual(sum_div(12), 6)
        self.assertEqual(sum_div(20), 10)
        self.assertEqual(sum_div(25), 14)
        self.assertEqual(sum_div(100), 44)
        self.assertEqual(sum_div(1000), 499)
