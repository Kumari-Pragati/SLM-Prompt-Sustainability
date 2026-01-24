import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(tn_gp(2, 3, 2), 8)
        self.assertEqual(tn_gp(5, 4, 3), 75)

    def test_zero_n(self):
        self.assertEqual(tn_gp(3, 0, 2), 0)

    def test_negative_n(self):
        self.assertRaises(ValueError, tn_gp, 4, -1, 2)

    def test_negative_r(self):
        self.assertRaises(ValueError, tn_gp, 5, 2, -3)

    def test_zero_r(self):
        self.assertRaises(ValueError, tn_gp, 6, 2, 0)
