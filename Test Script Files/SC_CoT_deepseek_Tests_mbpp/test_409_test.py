import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_typical_case(self):
        list1 = [(1, 2), (3, 4), (-1, -2)]
        self.assertEqual(min_product_tuple(list1), 2)

    def test_edge_case(self):
        list1 = [(0, 1), (2, 3), (4, 5)]
        self.assertEqual(min_product_tuple(list1), 0)

    def test_boundary_case(self):
        list1 = [(-1, 1), (-2, 2), (-3, 3)]
        self.assertEqual(min_product_tuple(list1), 2)

    def test_negative_numbers(self):
        list1 = [(-1, -2), (-3, -4), (-5, -6)]
        self.assertEqual(min_product_tuple(list1), 12)

    def test_large_numbers(self):
        list1 = [(1000000000, 1000000000), (-1000000000, -1000000000)]
        self.assertEqual(min_product_tuple(list1), 1000000000000000000)

    def test_invalid_input(self):
        list1 = [(1, 2), (3, 4), 'a']
        with self.assertRaises(TypeError):
            min_product_tuple(list1)
