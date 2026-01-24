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

    def test_even_numbers(self):
        self.assertEqual(smallest_multiple(4), 4)
        self.assertEqual(smallest_multiple(8), 8)
        self.assertEqual(smallest_multiple(12), 24)

    def test_odd_numbers(self):
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(5), 60)
        self.assertEqual(smallest_multiple(7), 140)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, smallest_multiple, -1)
