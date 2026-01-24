import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    def test_simple_even(self):
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(6), 2)

    def test_simple_odd(self):
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(3), 3)
        self.assertEqual(smallest_Divisor(5), 5)

    def test_edge_cases(self):
        self.assertEqual(smallest_Divisor(0), 0)
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(21), 7)
        self.assertEqual(smallest_Divisor(22), 2)

    def test_complex_cases(self):
        self.assertEqual(smallest_Divisor(20), 4)
        self.assertEqual(smallest_Divisor(28), 4)
        self.assertEqual(smallest_Divisor(49), 7)
        self.assertEqual(smallest_Divisor(62), 23)
