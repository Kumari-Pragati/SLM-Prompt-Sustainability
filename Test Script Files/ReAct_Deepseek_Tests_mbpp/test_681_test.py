import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    def test_smallest_Divisor_typical_cases(self):
        self.assertEqual(smallest_Divisor(7), 7)
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(13), 13)
        self.assertEqual(smallest_Divisor(15), 3)

    def test_smallest_Divisor_edge_cases(self):
        self.assertEqual(smallest_Divisor(2), 2)
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(0), 0)

    def test_smallest_Divisor_explicitly_handled_cases(self):
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(6), 2)
        self.assertEqual(smallest_Divisor(8), 2)
