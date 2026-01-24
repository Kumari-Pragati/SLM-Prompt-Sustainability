import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    def test_smallest_Divisor_even(self):
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(100), 2)

    def test_smallest_Divisor_odd(self):
        self.assertEqual(smallest_Divisor(9), 3)
        self.assertEqual(smallest_Divisor(11), 11)

    def test_smallest_Divisor_prime(self):
        self.assertEqual(smallest_Divisor(7), 7)
        self.assertEqual(smallest_Divisor(13), 13)

    def test_smallest_Divisor_large(self):
        self.assertEqual(smallest_Divisor(10000), 2)
        self.assertEqual(smallest_Divisor(681), 681)
