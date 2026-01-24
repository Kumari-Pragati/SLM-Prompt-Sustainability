import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):

    def test_positive_integer_arguments(self):
        self.assertEqual(tn_gp(2, 3, 2), 16)
        self.assertEqual(tn_gp(5, 4, 3), 60)

    def test_zero_as_base(self):
        self.assertEqual(tn_gp(3, 2, 0), 0)
        self.assertEqual(tn_gp(10, 3, 0), 0)

    def test_negative_base(self):
        self.assertRaises(ValueError, lambda: tn_gp(5, 3, -2))
        self.assertRaises(ValueError, lambda: tn_gp(-3, 2, -2))

    def test_negative_exponent(self):
        self.assertRaises(ValueError, lambda: tn_gp(2, -3, 2))
        self.assertRaises(ValueError, lambda: tn_gp(-2, -3, 2))

    def test_zero_exponent(self):
        self.assertEqual(tn_gp(3, 0, 2), 0)
        self.assertEqual(tn_gp(-3, 0, 2), 0)

    def test_zero_a(self):
        self.assertEqual(tn_gp(0, 3, 2), 0)
        self.assertEqual(tn_gp(-0, 3, 2), 0)
