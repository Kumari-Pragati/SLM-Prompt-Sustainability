import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(3), 3)
        self.assertEqual(sum_of_odd_Factors(5), 6)
        self.assertEqual(sum_of_odd_Factors(15), 243)
        self.assertEqual(sum_of_odd_Factors(21), 1365)

    def test_even_numbers(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(4), 4)
        self.assertEqual(sum_of_odd_Factors(6), 9)
        self.assertEqual(sum_of_odd_Factors(8), 15)
        self.assertEqual(sum_of_odd_Factors(10), 25)

    def test_prime_numbers(self):
        self.assertEqual(sum_of_odd_Factors(3), 3)
        self.assertEqual(sum_of_odd_Factors(5), 6)
        self.assertEqual(sum_of_odd_Factors(7), 7)
        self.assertEqual(sum_of_odd_Factors(11), 30)
        self.assertEqual(sum_of_odd_Factors(13), 231)

    def test_composite_numbers(self):
        self.assertEqual(sum_of_odd_Factors(9), 24)
        self.assertEqual(sum_of_odd_Factors(12), 27)
        self.assertEqual(sum_of_odd_Factors(18), 1365)
        self.assertEqual(sum_of_odd_Factors(24), 1365)
        self.assertEqual(sum_of_odd_Factors(36), 1365)

    def test_large_numbers(self):
        self.assertEqual(sum_of_odd_Factors(1000001), 1000001)
        self.assertEqual(sum_of_odd_Factors(1000003), 1000003)
        self.assertEqual(sum_of_odd_Factors(1000005), 1000005)
        self.assertEqual(sum_of_odd_Factors(1000007), 1000007)
        self.assertEqual(sum_of_odd_Factors(1000009), 1000009)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_of_odd_Factors, 0)
        self.assertRaises(TypeError, sum_of_odd_Factors, 'not a number')
