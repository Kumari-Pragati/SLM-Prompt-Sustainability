import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (-1, -2)]), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_product_tuple([(-1, -2), (-3, -4)]), 6)

    def test_positive_numbers(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4)]), 6)

    def test_zero_in_list(self):
        self.assertEqual(max_product_tuple([(0, 2), (3, 4)]), 0)

    def test_single_tuple(self):
        self.assertEqual(max_product_tuple([(1, 2)]), 2)

    def test_empty_list(self):
        self.assertEqual(max_product_tuple([]), 0)

    def test_negative_product(self):
        self.assertEqual(max_product_tuple([(-1, -2), (3, -4)]), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_product_tuple("invalid input")
