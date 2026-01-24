import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_neg([-1, -2, -3]), -1)

    def test_single_element(self):
        self.assertEqual(largest_neg([-5]), -5)

    def test_all_positive(self):
        self.assertEqual(largest_neg([1, 2, 3]), 1)

    def test_all_negative(self):
        self.assertEqual(largest_neg([-1, -2, -3]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(largest_neg([-1, 2, -3]), -1)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            largest_neg([])

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            largest_neg([-1, 'a', -3])
