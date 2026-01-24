import unittest
from mbpp_416_code import breakSum

class TestBreakSum(unittest.TestCase):

    def test_break_sum_small_numbers(self):
        self.assertEqual(breakSum(1), 1)
        self.assertEqual(breakSum(2), 1)
        self.assertEqual(breakSum(3), 1)
        self.assertEqual(breakSum(4), 2)
        self.assertEqual(breakSum(5), 2)
        self.assertEqual(breakSum(6), 1)
        self.assertEqual(breakSum(7), 2)
        self.assertEqual(breakSum(8), 3)
        self.assertEqual(breakSum(9), 4)
        self.assertEqual(breakSum(10), 3)

    def test_break_sum_large_numbers(self):
        self.assertEqual(breakSum(1000000), 1000000)

    def test_break_sum_max_value(self):
        self.assertEqual(breakSum(MAX), MAX)

    def test_break_sum_negative_numbers(self):
        self.assertRaises(ValueError, breakSum, -1)
        self.assertRaises(ValueError, breakSum, 0)
