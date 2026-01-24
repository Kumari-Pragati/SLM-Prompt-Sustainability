import unittest
from mbpp_55_code import tn_gp

class TestTnGp(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(tn_gp(10, 2, 0.5), 25.0)

    def test_zero_n(self):
        self.assertEqual(tn_gp(10, 0, 0.5), 0.0)

    def test_zero_r(self):
        self.assertEqual(tn_gp(10, 2, 0.0), 0.0)

    def test_negative_n(self):
        self.assertEqual(tn_gp(10, -2, 0.5), 0.0)

    def test_negative_r(self):
        self.assertEqual(tn_gp(10, 2, -0.5), 0.0)

    def test_non_integer_n(self):
        self.assertEqual(tn_gp(10, 2.5, 0.5), 25.0)

    def test_non_integer_r(self):
        self.assertEqual(tn_gp(10, 2, 0.5), 25.0)

    def test_non_numeric_a(self):
        with self.assertRaises(TypeError):
            tn_gp('ten', 2, 0.5)

    def test_non_numeric_n(self):
        with self.assertRaises(TypeError):
            tn_gp(10, 'two', 0.5)

    def test_non_numeric_r(self):
        with self.assertRaises(TypeError):
            tn_gp(10, 2, 'half')
