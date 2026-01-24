import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_count_fac_positive_integer(self):
        self.assertEqual(count_Fac(1), 1)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(6), 3)
        self.assertEqual(count_Fac(24), 6)
        self.assertEqual(count_Fac(120), 12)

    def test_count_fac_zero(self):
        self.assertEqual(count_Fac(0), 0)

    def test_count_fac_negative_integer(self):
        self.assertEqual(count_Fac(-1), 0)
        self.assertEqual(count_Fac(-2), 1)
        self.assertEqual(count_Fac(-21), 3)

    def test_count_fac_fraction(self):
        self.assertEqual(count_Fac(3.5), 1)
        self.assertEqual(count_Fac(5.5), 2)
        self.assertEqual(count_Fac(7.5), 3)

    def test_count_fac_large_number(self):
        self.assertEqual(count_Fac(1000000), 164134)

    def test_count_fac_prime_number(self):
        self.assertEqual(count_Fac(3), 1)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(7), 1)
        self.assertEqual(count_Fac(11), 1)
        self.assertEqual(count_Fac(13), 1)
