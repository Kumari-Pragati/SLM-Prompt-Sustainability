import unittest
from mbpp_354_code import tn_ap

class TestTNAP(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tn_ap(5, 10, 2), 25)

    def test_zero_difference(self):
        self.assertEqual(tn_ap(5, 0, 2), 5)

    def test_negative_difference(self):
        self.assertEqual(tn_ap(5, 10, -2), -5)

    def test_negative_start(self):
        self.assertEqual(tn_ap(-5, 10, 2), 15)

    def test_large_numbers(self):
        self.assertEqual(tn_ap(1000000000, 1000000000, 1), 2000000000000000000)

    def test_zero_start(self):
        self.assertEqual(tn_ap(0, 10, 2), 20)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            tn_ap(5, -10, 2)

    def test_zero_n(self):
        self.assertEqual(tn_ap(5, 0, 2), 5)
