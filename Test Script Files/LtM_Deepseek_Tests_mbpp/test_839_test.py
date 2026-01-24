import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sort_tuple(((2, 'b'), (1, 'a'))), ((1, 'a'), (2, 'b')))

    def test_edge_condition_empty_input(self):
        self.assertEqual(sort_tuple(()), ())

    def test_edge_condition_single_element(self):
        self.assertEqual(sort_tuple(((1, 'a'),)), ((1, 'a'),))

    def test_boundary_condition_minimum_value(self):
        self.assertEqual(sort_tuple(((0, 'a'), (1, 'b'))), ((0, 'a'), (1, 'b')))

    def test_boundary_condition_maximum_value(self):
        self.assertEqual(sort_tuple(((2, 'b'), (1, 'a'))), ((1, 'a'), (2, 'b')))

    def test_complex_case_duplicates(self):
        self.assertEqual(sort_tuple(((2, 'b'), (1, 'a'), (2, 'a'))), ((1, 'a'), (2, 'a'), (2, 'b')))

    def test_complex_case_reverse_order(self):
        self.assertEqual(sort_tuple(((3, 'c'), (2, 'b'), (1, 'a'))), ((1, 'a'), (2, 'b'), (3, 'c')))
