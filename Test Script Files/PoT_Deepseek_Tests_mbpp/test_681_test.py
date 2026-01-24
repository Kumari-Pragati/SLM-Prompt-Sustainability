import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(smallest_Divisor(7), 7)
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(15), 3)

    def test_edge_cases(self):
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(1), 1)

    def test_boundary_cases(self):
        self.assertEqual(smallest_Divisor(0), 0)
        self.assertEqual(smallest_Divisor(1000000007), 1000000007)

    def test_corner_cases(self):
        self.assertEqual(smallest_Divisor(3), 3)
        self.assertEqual(smallest_Divisor(8), 2)
