import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.assertEqual(sum(12, 16), 8)
        self.assertEqual(sum(28, 49), 28)
        self.assertEqual(sum(10, 2), 1)
        self.assertEqual(sum(1, 1), 0)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-12, -16), 12)
        self.assertEqual(sum(-28, -49), 28)
        self.assertEqual(sum(-10, -2), 1)
        self.assertEqual(sum(-1, -1), 0)

    def test_sum_zero(self):
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(0, 1), 0)
        self.assertEqual(sum(1, 0), 0)

    def test_sum_one_argument(self):
        self.assertEqual(sum(1), 0)
        self.assertEqual(sum(2), 0)
        self.assertEqual(sum(-1), 0)
