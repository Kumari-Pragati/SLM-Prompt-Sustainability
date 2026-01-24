import unittest
from mbpp_335_code import ap_sum

class TestArithmeticProgressionSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ap_sum(1, 5, 2), 14)

    def test_zero_elements(self):
        self.assertEqual(ap_sum(1, 0, 2), 0)

    def test_negative_elements(self):
        self.assertEqual(ap_sum(-1, 5, 2), 10)

    def test_zero_difference(self):
        self.assertEqual(ap_sum(1, 5, 0), 5)

    def test_large_numbers(self):
        self.assertEqual(ap_sum(1000, 100, 10), 50500)

    def test_negative_difference(self):
        self.assertEqual(ap_sum(1, 5, -2), -2)

    def test_negative_start(self):
        self.assertEqual(ap_sum(-1, 5, 2), 10)
