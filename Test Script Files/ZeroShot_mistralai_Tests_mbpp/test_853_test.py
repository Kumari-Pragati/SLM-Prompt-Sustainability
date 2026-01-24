import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)

    def test_simple_case(self):
        self.assertEqual(sum_of_odd_Factors(3), 3)

    def test_odd_prime_number(self):
        self.assertEqual(sum_of_odd_Factors(5), 5)
        self.assertEqual(sum_of_odd_Factors(7), 7)
        self.assertEqual(sum_of_odd_Factors(11), 11)

    def test_composite_odd_number(self):
        self.assertEqual(sum_of_odd_Factors(9), 10)
        self.assertEqual(sum_of_odd_Factors(15), 24)
        self.assertEqual(sum_of_odd_Factors(21), 42)

    def test_even_number(self):
        self.assertEqual(sum_of_odd_Factors(4), 4)
        self.assertEqual(sum_of_odd_Factors(6), 6)
        self.assertEqual(sum_of_odd_Factors(8), 8)
        self.assertEqual(sum_of_odd_Factors(10), 10)

    def test_large_number(self):
        self.assertEqual(sum_of_odd_Factors(1000003), 1000003)
