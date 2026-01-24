import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_gp(1, 3, 0.5), 3)
        self.assertEqual(sum_gp(5, 5, 0.25), 6.25)

    def test_zero_n(self):
        self.assertEqual(sum_gp(1, 0, 0.5), 1)
        self.assertEqual(sum_gp(-1, 0, 0.5), -1)

    def test_negative_r(self):
        self.assertRaises(ValueError, sum_gp, 1, 3, -1)

    def test_negative_a(self):
        self.assertRaises(ValueError, sum_gp, -1, 3, 0.5)
