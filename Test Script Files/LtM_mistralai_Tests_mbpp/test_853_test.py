import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_simple_odd_number(self):
        self.assertEqual(sum_of_odd_factors(3), 3)
        self.assertEqual(sum_of_odd_factors(5), 6)
        self.assertEqual(sum_of_odd_factors(7), 7)

    def test_even_number_with_single_odd_factor(self):
        self.assertEqual(sum_of_odd_factors(4), 4)
        self.assertEqual(sum_of_odd_factors(6), 7)
        self.assertEqual(sum_of_odd_factors(8), 8)

    def test_even_number_with_multiple_odd_factors(self):
        self.assertEqual(sum_of_odd_factors(10), 22)
        self.assertEqual(sum_of_odd_factors(12), 33)
        self.assertEqual(sum_of_odd_factors(14), 41)

    def test_square_number(self):
        self.assertEqual(sum_of_odd_factors(4), 4)
        self.assertEqual(sum_of_odd_factors(9), 24)
        self.assertEqual(sum_of_odd_factors(25), 151)

    def test_prime_number(self):
        self.assertEqual(sum_of_odd_factors(3), 3)
        self.assertEqual(sum_of_odd_factors(5), 6)
        self.assertEqual(sum_of_odd_factors(7), 7)
        self.assertEqual(sum_of_odd_factors(11), 11)
        self.assertEqual(sum_of_odd_factors(13), 13)
        self.assertEqual(sum_of_odd_factors(17), 17)

    def test_composite_number(self):
        self.assertEqual(sum_of_odd_factors(12), 33)
        self.assertEqual(sum_of_odd_factors(18), 61)
        self.assertEqual(sum_of_odd_factors(20), 71)

    def test_large_number(self):
        self.assertEqual(sum_of_odd_factors(1000001), 1000001)
        self.assertEqual(sum_of_odd_factors(1000003), 1000003)
        self.assertEqual(sum_of_odd_factors(1000005), 1000005)
