import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_gp(3, 5, 0.5), 15)
        self.assertEqual(sum_gp(10, 10, 0.2), 55)
        self.assertEqual(sum_gp(100, 20, 0.1), 1040)

    def test_zero_and_negative_numbers(self):
        self.assertAlmostEqual(sum_gp(0, 5, 0.5), 0)
        self.assertAlmostEqual(sum_gp(-3, 5, 0.5), -4.5)
        self.assertRaises(ValueError, sum_gp, 0, 0, 1)
        self.assertRaises(ValueError, sum_gp, -1, 5, 0.5)
        self.assertRaises(ValueError, sum_gp, 3, -5, 0.5)

    def test_r_greater_than_one(self):
        self.assertRaises(ValueError, sum_gp, 3, 5, 1.1)

    def test_r_equal_to_one(self):
        self.assertEqual(sum_gp(3, 5, 1), 3)

    def test_n_less_than_zero(self):
        self.assertRaises(ValueError, sum_gp, 3, -1, 0.5)
