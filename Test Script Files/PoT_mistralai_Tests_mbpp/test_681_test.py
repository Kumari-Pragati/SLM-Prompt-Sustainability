import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(smallest_Divisor(6), 2)
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(18), 2)
        self.assertEqual(smallest_Divisor(24), 2)
        self.assertEqual(smallest_Divisor(26), 13)
        self.assertEqual(smallest_Divisor(41), 41)
        self.assertEqual(smallest_Divisor(53), 53)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(smallest_Divisor(0), 0)
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(3), 3)
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(5), 5)
        self.assertEqual(smallest_Divisor(600851475143), 67)
