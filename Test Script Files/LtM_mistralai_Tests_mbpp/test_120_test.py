import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(max_product_tuple([1, 2, 3]), 6)

    def test_simple_negative(self):
        self.assertEqual(max_product_tuple([-1, -2, -3]), 6)

    def test_single_element(self):
        self.assertEqual(max_product_tuple([1]), 0)

    def test_empty_list(self):
        self.assertEqual(max_product_tuple([]), 0)

    def test_edge_case_min_product(self):
        self.assertEqual(max_product_tuple([-1, -2]), 2)

    def test_edge_case_max_product(self):
        self.assertEqual(max_product_tuple([100, 200]), 20000)

    def test_mixed_signs(self):
        self.assertEqual(max_product_tuple([1, -2, 3, -4]), 24)

    def test_large_numbers(self):
        self.assertEqual(max_product_tuple([1000000, 2000000]), 4000000000000)
