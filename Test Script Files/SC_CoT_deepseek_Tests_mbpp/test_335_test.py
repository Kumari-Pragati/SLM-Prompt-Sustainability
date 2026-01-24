import unittest
from mbpp_335_code import ap_sum

class TestArithmeticProgressionSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(ap_sum(1, 10, 2), 55)

    def test_single_term(self):
        self.assertAlmostEqual(ap_sum(1, 1, 2), 1)

    def test_zero_difference(self):
        self.assertAlmostEqual(ap_sum(1, 10, 0), 10)

    def test_negative_difference(self):
        self.assertAlmostEqual(ap_sum(1, 10, -2), 0)

    def test_large_numbers(self):
        self.assertAlmostEqual(ap_sum(1000000000, 1000000000, 1), 5000000005000000000)

    def test_negative_start(self):
        self.assertAlmostEqual(ap_sum(-1, 10, 2), 45)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            ap_sum(1, -10, 2)

    def test_invalid_d(self):
        with self.assertRaises(TypeError):
            ap_sum(1, 10, '2')
