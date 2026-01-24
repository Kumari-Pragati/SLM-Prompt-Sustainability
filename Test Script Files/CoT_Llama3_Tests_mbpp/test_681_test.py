import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(6), 2)
        self.assertEqual(smallest_Divisor(8), 2)
        self.assertEqual(smallest_Divisor(10), 2)

    def test_odd_numbers(self):
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(3), 3)
        self.assertEqual(smallest_Divisor(5), 5)
        self.assertEqual(smallest_Divisor(7), 7)

    def test_prime_numbers(self):
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(3), 3)
        self.assertEqual(smallest_Divisor(5), 5)
        self.assertEqual(smallest_Divisor(7), 7)

    def test_large_numbers(self):
        self.assertEqual(smallest_Divisor(100), 2)
        self.assertEqual(smallest_Divisor(101), 101)
        self.assertEqual(smallest_Divisor(102), 2)

    def test_edge_cases(self):
        self.assertEqual(smallest_Divisor(0), 0)
        self.assertEqual(smallest_Divisor(1), 1)
