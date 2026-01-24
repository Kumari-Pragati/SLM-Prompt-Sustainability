import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_product_tuple([]), 0)

    def test_single_element(self):
        self.assertEqual(min_product_tuple([1]), 0)
        self.assertEqual(min_product_tuple([-1]), 0)
        self.assertEqual(min_product_tuple([0]), 0)

    def test_positive_numbers(self):
        self.assertEqual(min_product_tuple([1, 2, 3]), 2)
        self.assertEqual(min_product_tuple([1, 2, -3]), 6)
        self.assertEqual(min_product_tuple([1, -2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(min_product_tuple([-1, -2, -3]), 6)
        self.assertEqual(min_product_tuple([-1, -2, 3]), 6)
        self.assertEqual(min_product_tuple([-1, 2, -3]), 12)

    def test_mixed_numbers(self):
        self.assertEqual(min_product_tuple([1, -2, 3, -4]), 12)
        self.assertEqual(min_product_tuple([1, 2, -3, 4]), 12)
        self.assertEqual(min_product_tuple([-1, 2, 3, -4]), 12)
