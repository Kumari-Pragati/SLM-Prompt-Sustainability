import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_gp(10, 5, 2), 38.5)
        self.assertEqual(sum_gp(50, 10, 3), 1666.6666666666668)

    def test_zero_and_negative_numbers(self):
        self.assertAlmostEqual(sum_gp(0, 5, 2), 0)
        self.assertAlmostEqual(sum_gp(-10, 5, 2), -20)
        self.assertAlmostEqual(sum_gp(0, 0, 2), 0)

    def test_r_greater_than_1(self):
        self.assertAlmostEqual(sum_gp(10, 5, 2.1), 18.444444444444443)

    def test_r_equal_to_1(self):
        self.assertEqual(sum_gp(10, 5, 1), 10)

    def test_n_less_than_0(self):
        self.assertRaises(ValueError, sum_gp, 10, -1, 2)

    def test_r_less_than_0(self):
        self.assertRaises(ValueError, sum_gp, 10, 5, -1)
