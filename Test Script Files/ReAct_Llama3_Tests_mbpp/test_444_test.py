import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 1), '[(2, 3), (5, 6)]')

    def test_edge_case_start(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 0), '[(1, 2, 3), (4, 5, 6)]')

    def test_edge_case_end(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 2), '[(1, 2), (4, 5)]')

    def test_edge_case_middle(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 1), '[(2, 3), (5, 6)]')

    def test_empty_list(self):
        self.assertEqual(trim_tuple([], 0), '[]')

    def test_single_element_list(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 0), '[(1, 2, 3)]')

    def test_single_element_list_edge_case(self):
        self.assertEqual(trim_tuple([(1, 2, 3)], 2), '[(1, 2)]')
