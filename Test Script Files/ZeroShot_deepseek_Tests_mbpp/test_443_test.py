import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_largest_neg(self):
        self.assertEqual(largest_neg([-1, -2, -3]), -1)
        self.assertEqual(largest_neg([1, -2, -3]), -2)
        self.assertEqual(largest_neg([1, 2, -3]), -3)
        self.assertEqual(largest_neg([0, 0, 0]), 0)
        self.assertEqual(largest_neg([-1]), -1)
        self.assertEqual(largest_neg([]), None)
