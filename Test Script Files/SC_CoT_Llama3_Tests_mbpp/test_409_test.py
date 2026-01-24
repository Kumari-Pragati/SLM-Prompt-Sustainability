import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (5, 6)]), min([abs(x*y) for x, y in [(1, 2), (3, 4), (5, 6)]]))

    def test_edge_case_negative(self):
        self.assertEqual(min_product_tuple([(-1, -2), (3, 4), (5, 6)]), min([abs(x*y) for x, y in [(-1, -2), (3, 4), (5, 6)]]))

    def test_edge_case_zero(self):
        self.assertEqual(min_product_tuple([(0, 0), (3, 4), (5, 6)]), min([abs(x*y) for x, y in [(0, 0), (3, 4), (5, 6)]]))

    def test_edge_case_positive(self):
        self.assertEqual(min_product_tuple([(1, 2), (0, 0), (5, 6)]), min([abs(x*y) for x, y in [(1, 2), (0, 0), (5, 6)]]))

    def test_empty_list(self):
        self.assertEqual(min_product_tuple([]), None)

    def test_single_element_list(self):
        self.assertEqual(min_product_tuple([(1, 2)]), min([abs(x*y) for x, y in [(1, 2)]]))

    def test_list_with_duplicates(self):
        self.assertEqual(min_product_tuple([(1, 2), (1, 2), (3, 4), (5, 6)]), min([abs(x*y) for x, y in [(1, 2), (1, 2), (3, 4), (5, 6)]]))
