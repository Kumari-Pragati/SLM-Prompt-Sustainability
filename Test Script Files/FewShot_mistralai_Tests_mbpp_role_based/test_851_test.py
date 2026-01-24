import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(Sum_of_Inverse_Divisors(4, 4), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(9, 3), 3.0)
        self.assertEqual(Sum_of_Inverse_Divisors(25, 5), 1.2)

    def test_zero(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(0, 0), 0.0)

    def test_negative_integer(self):
        self.assertRaises(ValueError, Sum_of_Inverse_Divisors, -5, 2.5)

    def test_non_integer(self):
        self.assertRaises(TypeError, Sum_of_Inverse_Divisors, 3.14, 2)
