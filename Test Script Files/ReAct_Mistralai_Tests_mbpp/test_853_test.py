import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(3), 3)
        self.assertEqual(sum_of_odd_Factors(5), 6)
        self.assertEqual(sum_of_odd_Factors(15), 22)
        self.assertEqual(sum_of_odd_Factors(21), 105)

    def test_even_numbers(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(4), 4)
        self.assertEqual(sum_of_odd_Factors(6), 6)
        self.assertEqual(sum_of_odd_Factors(8), 8)
        self.assertEqual(sum_of_odd_Factors(10), 22)

    def test_prime_numbers(self):
        self.assertEqual(sum_of_odd_Factors(7), 7)
        self.assertEqual(sum_of_odd_Factors(11), 11)
        self.assertEqual(sum_of_odd_Factors(13), 24)
        self.assertEqual(sum_of_odd_Factors(17), 17)
        self.assertEqual(sum_of_odd_Factors(19), 38)

    def test_square_numbers(self):
        self.assertEqual(sum_of_odd_Factors(4), 4)
        self.assertEqual(sum_of_odd_Factors(9), 24)
        self.assertEqual(sum_of_odd_Factors(16), 48)
        self.assertEqual(sum_of_odd_Factors(25), 150)
        self.assertEqual(sum_of_odd_Factors(36), 168)

    def test_large_numbers(self):
        self.assertEqual(sum_of_odd_Factors(1000001), 1000001)
        self.assertEqual(sum_of_odd_Factors(1000003), 1000003)
        self.assertEqual(sum_of_odd_Factors(1000005), 2000001)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, sum_of_odd_Factors, -1)
        self.assertRaises(ValueError, sum_of_odd_Factors, -2)
        self.assertRaises(ValueError, sum_of_odd_Factors, -3)
