import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1]), [1])
        self.assertListEqual(extract_index_list([2, 2, 3], [2, 2, 3], [2, 2, 3]), [2])
        self.assertListEqual(extract_index_list([4, 4, 4], [4, 4, 4], [4, 4, 4]), [4])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(extract_index_list([], [], []), [])
        self.assertListEqual(extract_index_list([1], [1], []), [])
        self.assertListEqual(extract_index_list([1, 1], [1], []), [])
        self.assertListEqual(extract_index_list([1, 1, 1], [2], []), [])
        self.assertListEqual(extract_index_list([1, 1, 1], [1, 2], []), [])
        self.assertListEqual(extract_index_list([1, 1, 1], [1, 1, 2], []), [1])
        self.assertListEqual(extract_index_list([1, 1, 1], [1, 1, 1, 1], [1, 1, 1]), [1])
        self.assertListEqual(extract_index_list([1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1]), [1])

    def test_special_cases(self):
        self.assertListEqual(extract_index_list([1, 2, 1], [2, 1, 2], [1, 2, 1]), [1])
        self.assertListEqual(extract_index_list([1, 1, 2], [1, 2, 1], [2, 1, 1]), [])
        self.assertListEqual(extract_index_list([1, 1, 1], [1, 2, 2], [1, 2, 2]), [])
        self.assertListEqual(extract_index_list([1, 1, 1], [2, 1, 2], [2, 1, 1]), [])
