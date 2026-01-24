import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 1)
        self.assertEqual(sum_div(3), 2)
        self.assertEqual(sum_div(4), 3)
        self.assertEqual(sum_div(5), 3)
        self.assertEqual(sum_div(6), 6)

    def test_edge(self):
        self.assertEqual(sum_div(0), 0)
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(10), 18)
        self.assertEqual(sum_div(20), 42)
        self.assertEqual(sum_div(100), 454)

    def test_edge2(self):
        self.assertEqual(sum_div(2), 1)
        self.assertEqual(sum_div(3), 2)
        self.assertEqual(sum_div(4), 3)
        self.assertEqual(sum_div(5), 3)
        self.assertEqual(sum_div(6), 6)

    def test_edge3(self):
        self.assertEqual(sum_div(7), 12)
        self.assertEqual(sum_div(8), 6)
        self.assertEqual(sum_div(9), 10)
        self.assertEqual(sum_div(10), 18)
        self.assertEqual(sum_div(11), 12)
