import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):
    def test_small_positive_numbers(self):
        self.assertEqual(breakSum(3), 1)
        self.assertEqual(breakSum(4), 2)
        self.assertEqual(breakSum(5), 3)
        self.assertEqual(breakSum(6), 3)
        self.assertEqual(breakSum(7), 4)
        self.assertEqual(breakSum(8), 3)
        self.assertEqual(breakSum(9), 4)
        self.assertEqual(breakSum(10), 5)

    def test_large_positive_numbers(self):
        self.assertEqual(breakSum(1000), 1000)
        self.assertEqual(breakSum(10000), 10000)
        self.assertEqual(breakSum(100000), 100000)
        self.assertEqual(breakSum(1000000), 1000000)

    def test_zero(self):
        self.assertEqual(breakSum(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(breakSum(-1), 1)
        self.assertEqual(breakSum(-2), 1)
        self.assertEqual(breakSum(-3), 2)
        self.assertEqual(breakSum(-4), 2)
        self.assertEqual(breakSum(-5), 3)
        self.assertEqual(breakSum(-6), 3)
        self.assertEqual(breakSum(-7), 4)
        self.assertEqual(breakSum(-8), 3)
        self.assertEqual(breakSum(-9), 4)
        self.assertEqual(breakSum(-10), 5)

    def test_large_negative_numbers(self):
        self.assertEqual(breakSum(-1000), 1000)
        self.assertEqual(breakSum(-10000), 10000)
        self.assertEqual(breakSum(-100000), 100000)
        self.assertEqual(breakSum(-1000000), 1000000)
