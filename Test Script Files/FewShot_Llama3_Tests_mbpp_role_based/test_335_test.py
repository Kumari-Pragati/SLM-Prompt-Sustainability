import unittest
from mbpp_335_code import ap_sum

class TestApSum(unittest.TestCase):
    def test_ap_sum_positive_numbers(self):
        self.assertEqual(ap_sum(1, 5, 2), 15)

    def test_ap_sum_zero(self):
        self.assertEqual(ap_sum(0, 0, 0), 0)

    def test_ap_sum_negative_numbers(self):
        self.assertEqual(ap_sum(-1, 5, 2), -15)

    def test_ap_sum_non_integer_numbers(self):
        self.assertEqual(ap_sum(1.5, 5, 2), 12.5)

    def test_ap_sum_non_positive_n(self):
        self.assertEqual(ap_sum(1, 0, 2), 0)

    def test_ap_sum_non_positive_d(self):
        self.assertEqual(ap_sum(1, 5, -2), 5)

    def test_ap_sum_invalid_input(self):
        with self.assertRaises(TypeError):
            ap_sum('a', 5, 2)
