import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)
        self.assertEqual(count_odd([10, 20, 30, 40, 50]), 0)
        self.assertEqual(count_odd([1, 3, 5, 7, 9]), 5)
        self.assertEqual(count_odd([2, 4, 6, 8, 10]), 0)

    def test_empty(self):
        self.assertEqual(count_odd([]), 0)

    def test_single(self):
        self.assertEqual(count_odd([1]), 1)
        self.assertEqual(count_odd([2]), 0)

    def test_negative(self):
        self.assertEqual(count_odd([-1, -2, -3, -4, -5]), 3)
        self.assertEqual(count_odd([-10, -20, -30, -40, -50]), 0)

    def test_mixed(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
        self.assertEqual(count_odd([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]), 5)
