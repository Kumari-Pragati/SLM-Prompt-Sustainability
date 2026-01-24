import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):
    def test_smallest_multiple_positive(self):
        self.assertEqual(smallest_multiple(1), 2)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 4)
        self.assertEqual(smallest_multiple(5), 10)
        self.assertEqual(smallest_multiple(6), 6)
        self.assertEqual(smallest_multiple(7), 14)
        self.assertEqual(smallest_multiple(8), 8)
        self.assertEqual(smallest_multiple(9), 18)
        self.assertEqual(smallest_multiple(10), 20)
        self.assertEqual(smallest_multiple(12), 12)
        self.assertEqual(smallest_multiple(15), 30)
        self.assertEqual(smallest_multiple(20), 20)

    def test_smallest_multiple_large_numbers(self):
        self.assertEqual(smallest_multiple(100), 200)
        self.assertEqual(smallest_multiple(1000), 2000)
        self.assertEqual(smallest_multiple(10000), 20000)
        self.assertEqual(smallest_multiple(100000), 200000)

    def test_smallest_multiple_negative(self):
        self.assertEqual(smallest_multiple(-1), None)
        self.assertEqual(smallest_multiple(-2), -2)

    def test_smallest_multiple_zero(self):
        self.assertEqual(smallest_multiple(0), 0)
