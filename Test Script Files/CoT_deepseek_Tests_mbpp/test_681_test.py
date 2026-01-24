import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(100), 2)
        self.assertEqual(smallest_Divisor(200), 2)

    def test_odd_numbers(self):
        self.assertEqual(smallest_Divisor(97), 97)
        self.assertEqual(smallest_Divisor(199), 199)

    def test_prime_numbers(self):
        self.assertEqual(smallest_Divisor(7), 7)
        self.assertEqual(smallest_Divisor(13), 13)

    def test_numbers_with_divisors(self):
        self.assertEqual(smallest_Divisor(15), 3)
        self.assertEqual(smallest_Divisor(21), 3)

    def test_edge_cases(self):
        self.assertEqual(smallest_Divisor(0), 0)
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(3), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            smallest_Divisor('a')
        with self.assertRaises(ValueError):
            smallest_Divisor(-5)
