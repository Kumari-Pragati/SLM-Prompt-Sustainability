import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Fac(0), 0)

    def test_one(self):
        self.assertEqual(count_Fac(1), 0)

    def test_prime_number(self):
        self.assertEqual(count_Fac(2), 0)

    def test_composite_number(self):
        self.assertEqual(count_Fac(4), 2)

    def test_large_number(self):
        self.assertEqual(count_Fac(100), 2)

    def test_perfect_square(self):
        self.assertEqual(count_Fac(36), 3)

    def test_perfect_cube(self):
        self.assertEqual(count_Fac(27), 3)

    def test_perfect_power(self):
        self.assertEqual(count_Fac(81), 3)

    def test_large_perfect_power(self):
        self.assertEqual(count_Fac(243), 4)
