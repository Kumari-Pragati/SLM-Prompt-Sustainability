import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [(1, 2), (3, 4), (-1, -2), (-3, -4)]
        self.assertEqual(max_product_tuple(list1), 8)

    def test_edge_case(self):
        list1 = [(0, 0)]
        self.assertEqual(max_product_tuple(list1), 0)

    def test_boundary_case(self):
        list1 = [(1, 1), (-1, -1)]
        self.assertEqual(max_product_tuple(list1), 1)

    def test_negative_numbers(self):
        list1 = [(-1, -2), (-3, -4)]
        self.assertEqual(max_product_tuple(list1), 6)

    def test_positive_numbers(self):
        list1 = [(1, 2), (3, 4)]
        self.assertEqual(max_product_tuple(list1), 6)

    def test_invalid_input(self):
        list1 = [(1, 2), 'a', (-3, -4)]
        with self.assertRaises(TypeError):
            max_product_tuple(list1)
