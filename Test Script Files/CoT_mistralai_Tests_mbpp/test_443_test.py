import unittest
from443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(largest_neg([]), float('-inf'))

    def test_single_element_list(self):
        for num in [-1, 0, 1]:
            self.assertEqual(largest_neg([num]), num)

    def test_positive_list(self):
        self.assertEqual(largest_neg([1, 2, -3, -4, -5]), -5)

    def test_negative_list(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5]), -1)

    def test_mixed_list(self):
        self.assertEqual(largest_neg([1, -2, 3, -4, 5]), -4)

    def test_float_list(self):
        self.assertEqual(largest_neg([-3.14, -2, -1, 0, 1]), -3.14)

    def test_list_with_zero(self):
        self.assertEqual(largest_neg([0, -1, 0, -2, 0]), -2)
