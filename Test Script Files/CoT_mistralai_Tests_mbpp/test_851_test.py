import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(Sum_of_Inverse_Divisors(4, 10), 2.5)
        self.assertEqual(Sum_of_Inverse_Divisors(8, 3.5), 1.5)
        self.assertEqual(Sum_of_Inverse_Divisors(220, 250), 1.12)

    def test_zero(self):
        self.assertRaises(ValueError, Sum_of_Inverse_Divisors, 0, 10)

    def test_negative_integer(self):
        self.assertRaises(ValueError, Sum_of_Inverse_Divisors, -5, 10)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, Sum_of_Inverse_Divisors, 'str', 10)
        self.assertRaises(TypeError, Sum_of_Inverse_Divisors, 10, 'str')
