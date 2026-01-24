import unittest
from mbpp_55_code import tn_gp
import math

class TestTnGp(unittest.TestCase):

    def test_tn_gp_with_positive_values(self):
        self.assertEqual(tn_gp(2, 3, 3), 54)
        self.assertEqual(tn_gp(5, 4, 2), 50)
        self.assertEqual(tn_gp(10, 5, 3), 900)

    def test_tn_gp_with_zero_base(self):
        self.assertEqual(tn_gp(0, 3, 3), 0)

    def test_tn_gp_with_negative_values(self):
        with self.assertRaises(ValueError):
            tn_gp(-1, 3, 3)
        with self.assertRaises(ValueError):
            tn_gp(1, -1, 3)
        with self.assertRaises(ValueError):
            tn_gp(1, 3, -1)

    def test_tn_gp_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            tn_gp(2, 3.5, 3)
        with self.assertRaises(TypeError):
            tn_gp(2, 3, 3.5)
