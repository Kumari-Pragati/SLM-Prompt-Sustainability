import unittest
from681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    def test_smallest_divisor_even(self):
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(6), 2)

    def test_smallest_divisor_odd_prime(self):
        self.assertEqual(smallest_Divisor(3), 3)
        self.assertEqual(smallest_Divisor(5), 5)
        self.assertEqual(smallest_Divisor(7), 7)

    def test_smallest_divisor_odd_composite(self):
        self.assertEqual(smallest_Divisor(9), 3)
        self.assertEqual(smallest_Divisor(15), 3)
        self.assertEqual(smallest_Divisor(21), 3)

    def test_smallest_divisor_large_numbers(self):
        self.assertEqual(smallest_Divisor(100), 2)
        self.assertEqual(smallest_Divisor(1000), 2)
        self.assertEqual(smallest_Divisor(10000), 2)
