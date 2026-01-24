import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)
        self.assertEqual(first_odd([10, 20, 30, 40, 50]), -1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
        self.assertEqual(first_odd([1, 3, 5, 7, 9]), 1)

    def test_empty(self):
        self.assertEqual(first_odd([]), -1)

    def test_single(self):
        self.assertEqual(first_odd([1]), 1)
        self.assertEqual(first_odd([2]), -1)
        self.assertEqual(first_odd([3]), 3)

    def test_multiple(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
        self.assertEqual(first_odd([1, 3, 5, 7, 9]), 1)

    def test_negative(self):
        self.assertEqual(first_odd([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(first_odd([-2, -4, -6, -8, -10]), -1)
        self.assertEqual(first_odd([-1, -3, -5, -7, -9]), -1)
