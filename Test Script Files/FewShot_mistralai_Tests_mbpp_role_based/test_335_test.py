import unittest
from mbpp_335_code import ap_sum

class TestAPSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(ap_sum(1, 5, 2), 15)
        self.assertEqual(ap_sum(2, 3, 1), 7)

    def test_zero_n(self):
        self.assertEqual(ap_sum(0, 0, 0), 0)
        self.assertEqual(ap_sum(1, 0, 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(ap_sum(-1, 5, 2), -5)
        self.assertEqual(ap_sum(-2, 3, -1), -7)

    def test_negative_d(self):
        self.assertEqual(ap_sum(1, 5, -2), -15)
        self.assertEqual(ap_sum(2, 3, -1), -7)
