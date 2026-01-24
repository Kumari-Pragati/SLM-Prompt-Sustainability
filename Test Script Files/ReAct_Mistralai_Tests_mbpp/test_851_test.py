import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(Sum_of_Inverse_Divisors(4, 10), 2.0)
        self.assertEqual(Sum_of_InverseDivisors(25, 100), 2.5)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Sum_of_InverseDivisors(0, 10)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            Sum_of_InverseDivisors(-5, 10)

    def test_non_numeric_sum(self):
        with self.assertRaises(TypeError):
            Sum_of_InverseDivisors(4, 'str')

    def test_non_numeric_number(self):
        with self.assertRaises(TypeError):
            Sum_of_InverseDivisors('5', 10)

    def test_floating_point_number(self):
        self.assertAlmostEqual(Sum_of_InverseDivisors(3, 3.5), 1.17)

    def test_large_number(self):
        self.assertAlmostEqual(Sum_of_InverseDivisors(1000000, 1000000), 1.0)
