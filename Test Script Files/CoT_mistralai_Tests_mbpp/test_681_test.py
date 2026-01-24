import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(18), 2)
        self.assertEqual(smallest_Divisor(20), 4)
        self.assertEqual(smallest_Divisor(91), 7)
        self.assertEqual(smallest_Divisor(221), 7)

    def test_even_numbers(self):
        self.assertEqual(smallest_Divisor(6), 2)
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(12), 2)

    def test_prime_numbers(self):
        self.assertEqual(smallest_Divisor(3), 3)
        self.assertEqual(smallest_Divisor(5), 5)
        self.assertEqual(smallest_Divisor(7), 7)
        self.assertEqual(smallest_Divisor(11), 11)
        self.assertEqual(smallest_Divisor(13), 13)

    def test_square_numbers(self):
        self.assertEqual(smallest_Divisor(9), 3)
        self.assertEqual(smallest_Divisor(16), 4)
        self.assertEqual(smallest_Divisor(25), 5)

    def test_edge_cases(self):
        self.assertEqual(smallest_Divisor(0), 0)
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(2), 2)
