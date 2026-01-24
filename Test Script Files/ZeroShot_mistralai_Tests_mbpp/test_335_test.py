import unittest
from mbpp_335_code import ap_sum

class TestAPSum(unittest.TestCase):

    def test_ap_sum_with_positive_values(self):
        self.assertEqual(ap_sum(1, 5, 2), 15)
        self.assertEqual(ap_sum(2, 3, 1), 12)
        self.assertEqual(ap_sum(3, 4, 2), 24)

    def test_ap_sum_with_zero_values(self):
        self.assertEqual(ap_sum(0, 5, 2), 10)
        self.assertEqual(ap_sum(0, 3, 1), 6)
        self.assertEqual(ap_sum(0, 4, 2), 12)

    def test_ap_sum_with_negative_values(self):
        self.assertEqual(ap_sum(-1, 5, 2), -15)
        self.assertEqual(ap_sum(-2, 3, 1), -12)
        self.assertEqual(ap_sum(-3, 4, 2), -24)

    def test_ap_sum_with_negative_d(self):
        self.assertEqual(ap_sum(1, 5, -2), -15)
        self.assertEqual(ap_sum(2, 3, -1), -12)
        self.assertEqual(ap_sum(3, 4, -2), -24)

    def test_ap_sum_with_negative_n(self):
        self.assertEqual(ap_sum(1, -5, 2), -15)
        self.assertEqual(ap_sum(2, -3, 1), -12)
        self.assertEqual(ap_sum(3, -4, 2), -24)
