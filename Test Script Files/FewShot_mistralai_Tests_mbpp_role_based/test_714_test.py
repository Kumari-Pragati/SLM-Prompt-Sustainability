import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(count_Fac(4), 3)
        self.assertEqual(count_Fac(10), 4)
        self.assertEqual(count_Fac(20), 8)

    def test_zero(self):
        self.assertEqual(count_Fac(0), 0)

    def test_negative_integer(self):
        self.assertEqual(count_Fac(-1), 0)

    def test_one(self):
        self.assertEqual(count_Fac(1), 1)

    def test_large_integer(self):
        self.assertEqual(count_Fac(100000), 164937)

    def test_fraction(self):
        with self.assertRaises(ValueError):
            count_Fac(0.5)
