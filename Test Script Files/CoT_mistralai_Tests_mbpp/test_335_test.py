import unittest
from mbpp_335_code import ap_sum

class TestAPSum(unittest.TestCase):
    def test_ap_sum_positive(self):
        self.assertEqual(ap_sum(1, 5, 2), 20)
        self.assertEqual(ap_sum(3, 3, 1), 18)
        self.assertEqual(ap_sum(5, 10, 3), 165)

    def test_ap_sum_zero(self):
        self.assertEqual(ap_sum(0, 5, 2), 6)
        self.assertEqual(ap_sum(0, 0, 0), 0)

    def test_ap_sum_negative(self):
        self.assertEqual(ap_sum(-1, 5, 2), -10)
        self.assertEqual(ap_sum(-3, 3, -1), -18)

    def test_ap_sum_invalid_n(self):
        self.assertRaises(ValueError, ap_sum, 1, 0, 2)
        self.assertRaises(ValueError, ap_sum, 1, -1, 2)

    def test_ap_sum_invalid_d(self):
        self.assertRaises(ValueError, ap_sum, 1, 5, 0)
