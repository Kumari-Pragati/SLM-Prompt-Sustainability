import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum(4, 6), 2)
        self.assertEqual(sum(8, 2), 2)
        self.assertEqual(sum(12, 3), 3)
        self.assertEqual(sum(18, 2), 6)

    def test_negative_numbers(self):
        self.assertEqual(sum(-4, -6), 4)
        self.assertEqual(sum(-8, -2), 2)
        self.assertEqual(sum(-12, -3), 3)
        self.assertEqual(sum(-18, -2), 6)

    def test_zero(self):
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(0, 4), 0)
        self.assertEqual(sum(4, 0), 0)

    def test_one_argument(self):
        self.assertEqual(sum(4), 0)
        self.assertEqual(sum(0), 0)
        self.assertEqual(sum(-4), 0)

    def test_large_numbers(self):
        self.assertEqual(sum(1000000, 999999), 999998)
        self.assertEqual(sum(999999, 1000000), 999998)

    def test_edge_cases(self):
        self.assertEqual(sum(1, 1), 0)
        self.assertEqual(sum(2, 1), 1)
        self.assertEqual(sum(1, 2), 1)
