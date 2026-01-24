import unittest
from mbpp_491_code import pow
from forty_nine_one_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_sum_gp_with_positive_values(self):
        self.assertEqual(sum_gp(10, 3, 2), 38.0)
        self.assertEqual(sum_gp(50, 5, 3), 1687.5)
        self.assertEqual(sum_gp(100, 10, 2), 5050.0)

    def test_sum_gp_with_zero_r(self):
        with self.assertRaises(ZeroDivisionError):
            sum_gp(10, 3, 0)

    def test_sum_gp_with_negative_values(self):
        with self.assertRaises(ValueError):
            sum_gp(-10, 3, 2)
        with self.assertRaises(ValueError):
            sum_gp(10, -3, 2)
        with self.assertRaises(ValueError):
            sum_gp(10, 3, -2)

    def test_sum_gp_with_non_integer_n(self):
        with self.assertRaises(TypeError):
            sum_gp(10, 3.5, 2)
