import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(min_product_tuple([(1, 2), (3, 4), (-1, -2)]), 2)

    def test_negative_numbers(self):
        self.assertAlmostEqual(min_product_tuple([(-1, -2), (-3, -4)]), 4)

    def test_positive_numbers(self):
        self.assertAlmostEqual(min_product_tuple([(1, 2), (3, 4)]), 2)

    def test_zero_numbers(self):
        self.assertAlmostEqual(min_product_tuple([(0, 2), (3, 4)]), 0)

    def test_single_tuple(self):
        self.assertAlmostEqual(min_product_tuple([(1, 2)]), 2)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            min_product_tuple([])

    def test_non_tuple_elements(self):
        with self.assertRaises(TypeError):
            min_product_tuple([(1, 2), 'a', (3, 4)])

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            min_product_tuple([(1.5, 2), (3, 4)])
