import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(tn_ap(1, 3, 2), 6)
        self.assertEqual(tn_ap(5, 4, 1), 10)

    def test_zero_n(self):
        self.assertEqual(tn_ap(0, 0, 1), 0)

    def test_negative_n(self):
        self.assertEqual(tn_ap(2, -1, 1), -1)

    def test_negative_d(self):
        self.assertEqual(tn_ap(3, 2, -1), 1)

    def test_zero_d(self):
        self.assertEqual(tn_ap(4, 3, 0), 4)

    def test_negative_a(self):
        self.assertEqual(tn_ap(-1, 2, 1), -3)
