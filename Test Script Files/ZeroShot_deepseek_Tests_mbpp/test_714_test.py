import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_count_Fac_positive_numbers(self):
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 1)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(6), 2)
        self.assertEqual(count_Fac(7), 1)
        self.assertEqual(count_Fac(8), 3)
        self.assertEqual(count_Fac(9), 2)
        self.assertEqual(count_Fac(10), 2)

    def test_count_Fac_negative_numbers(self):
        self.assertEqual(count_Fac(-1), 0)
        self.assertEqual(count_Fac(-2), 0)
        self.assertEqual(count_Fac(-3), 0)
        self.assertEqual(count_Fac(-4), 0)
        self.assertEqual(count_Fac(-5), 0)
        self.assertEqual(count_Fac(-6), 0)
        self.assertEqual(count_Fac(-7), 0)
        self.assertEqual(count_Fac(-8), 0)
        self.assertEqual(count_Fac(-9), 0)
        self.assertEqual(count_Fac(-10), 0)

    def test_count_Fac_zero(self):
        self.assertEqual(count_Fac(0), 0)
