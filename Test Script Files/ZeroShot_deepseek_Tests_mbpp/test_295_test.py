import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_sum_div_1(self):
        self.assertEqual(sum_div(1), 1)

    def test_sum_div_2(self):
        self.assertEqual(sum_div(6), 6)

    def test_sum_div_3(self):
        self.assertEqual(sum_div(28), 28)

    def test_sum_div_4(self):
        self.assertEqual(sum_div(12), 1+2+3+4+6)

    def test_sum_div_5(self):
        self.assertEqual(sum_div(36), 1+2+3+4+6+9+12+18)
