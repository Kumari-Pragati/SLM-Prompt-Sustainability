import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_edge_case_empty_lists(self):
        self.assertEqual(extract_index_list([], [], []), [])

    def test_boundary_case_different_lengths(self):
        self.assertEqual(extract_index_list([1, 2], [1, 2, 3], [1, 2]), [1, 2])

    def test_corner_case_all_different(self):
        self.assertEqual(extract_index_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [])

    def test_corner_case_all_same(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1]), [1, 1, 1])
