import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_sum_div(self):
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(2), 1)
        self.assertEqual(sum_div(3), 2)
        self.assertEqual(sum_div(4), 3)
        self.assertEqual(sum_div(5), 3)
        self.assertEqual(sum_div(6), 6)
        self.assertEqual(sum_div(7), 3)
        self.assertEqual(sum_div(8), 6)
        self.assertEqual(sum_div(9), 6)
        self.assertEqual(sum_div(10), 8)
        self.assertEqual(sum_div(11), 3)
        self.assertEqual(sum_div(12), 6)
        self.assertEqual(sum_div(13), 3)
        self.assertEqual(sum_div(14), 6)
        self.assertEqual(sum_div(15), 8)
        self.assertEqual(sum_div(16), 6)
        self.assertEqual(sum_div(17), 3)
        self.assertEqual(sum_div(18), 6)
        self.assertEqual(sum_div(19), 3)
        self.assertEqual(sum_div(20), 6)
