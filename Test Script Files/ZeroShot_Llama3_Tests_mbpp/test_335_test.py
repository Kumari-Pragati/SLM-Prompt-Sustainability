import unittest
from mbpp_335_code import ap_sum

class TestApSum(unittest.TestCase):

    def test_ap_sum_positive(self):
        self.assertEqual(ap_sum(1, 5, 2), 9)

    def test_ap_sum_negative(self):
        self.assertEqual(ap_sum(-1, 5, 2), -9)

    def test_ap_sum_zero(self):
        self.assertEqual(ap_sum(0, 5, 2), 0)

    def test_ap_sum_non_integer(self):
        self.assertEqual(ap_sum(1.5, 5, 2), 9.5)

    def test_ap_sum_non_positive(self):
        self.assertEqual(ap_sum(-1, -5, 2), 9)

    def test_ap_sum_non_integer_negative(self):
        self.assertEqual(ap_sum(-1.5, -5, 2), -9.5)

    def test_ap_sum_non_integer_zero(self):
        self.assertEqual(ap_sum(0.5, 5, 2), 0.5)

    def test_ap_sum_non_integer_positive(self):
        self.assertEqual(ap_sum(1.5, 5, 2), 9.5)
