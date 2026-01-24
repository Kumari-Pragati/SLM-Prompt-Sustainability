import unittest
from mbpp_354_code import tn_ap

class TestTNAP(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(tn_ap(2, 5, 3), 13)
        self.assertEqual(tn_ap(1, 10, 1), 10)
        self.assertEqual(tn_ap(10, 5, 2), 24)

    def test_negative_numbers(self):
        self.assertEqual(tn_ap(-2, 5, 3), 7)
        self.assertEqual(tn_ap(-1, 10, 1), 9)
        self.assertEqual(tn_ap(-10, 5, 2), 0)

    def test_zero_difference(self):
        self.assertEqual(tn_ap(1, 5, 0), 1)
        self.assertEqual(tn_ap(0, 10, 0), 0)

    def test_zero_start(self):
        self.assertEqual(tn_ap(0, 5, 3), 12)

    def test_zero_input(self):
        self.assertEqual(tn_ap(0, 0, 0), 0)
