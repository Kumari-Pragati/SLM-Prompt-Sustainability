import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_product_tuple([]), 0)

    def test_single_element_list(self):
        self.assertEqual(min_product_tuple([1]), 0)
        self.assertEqual(min_product_tuple([-1]), 0)

    def test_positive_numbers(self):
        self.assertEqual(min_product_tuple([1, 2, 3]), 0)
        self.assertEqual(min_product_tuple([10, 20, 30]), 600)

    def test_negative_numbers(self):
        self.assertEqual(min_product_tuple([-1, -2, -3]), 6)
        self.assertEqual(min_product_tuple([-10, -20, -30]), 6000)

    def test_mixed_numbers(self):
        self.assertEqual(min_product_tuple([1, -2, 3]), 0)
        self.assertEqual(min_product_tuple([-1, 2, -3]), 12)
        self.assertEqual(min_product_tuple([10, -20, 30]), -6000)

    def test_large_numbers(self):
        self.assertEqual(min_product_tuple([1000000, 2000000, 3000000]), 6000000000000)

    def test_zero(self):
        self.assertEqual(min_product_tuple([0, 1]), 0)
        self.assertEqual(min_product_tuple([0, -1]), 0)
        self.assertEqual(min_product_tuple([0, 0]), 0)
