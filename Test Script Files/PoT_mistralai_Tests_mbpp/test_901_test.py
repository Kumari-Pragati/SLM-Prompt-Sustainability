import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)

    def test_large_numbers(self):
        self.assertEqual(smallest_multiple(10), 240)
        self.assertEqual(smallest_multiple(100), 232792560)
        self.assertEqual(smallest_multiple(1000), 232792560000)

    def test_edge_cases(self):
        self.assertEqual(smallest_multiple(0), 0)
        self.assertEqual(smallest_multiple(1000000), 232792560000)
        self.assertEqual(smallest_multiple(2147483647), 4294967296)
