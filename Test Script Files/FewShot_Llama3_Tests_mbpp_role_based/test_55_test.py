import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(tn_gp(10, 5, 0.05), 10 * (1 + 0.05)**4)

    def test_zero_rate(self):
        self.assertEqual(tn_gp(10, 5, 0), 0)

    def test_zero_periods(self):
        self.assertEqual(tn_gp(10, 0, 0.05), 10)

    def test_negative_periods(self):
        with self.assertRaises(TypeError):
            tn_gp(10, -5, 0.05)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            tn_gp('ten', 5, 0.05)
