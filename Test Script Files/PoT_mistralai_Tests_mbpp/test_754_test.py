import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1]), [1])

    def test_edge_case_1(self):
        self.assertListEqual(extract_index_list([1, 2, 1], [2, 1, 2], [1, 2, 1]), [])

    def test_edge_case_2(self):
        self.assertListEqual(extract_index_list([1, 1], [1, 1], [1, 1]), [1])

    def test_edge_case_3(self):
        self.assertListEqual(extract_index_list([1, 1, 2], [1, 1, 1], [1, 1, 1]), [])

    def test_corner_case_1(self):
        self.assertListEqual(extract_index_list([], [], []), [])

    def test_corner_case_2(self):
        self.assertListEqual(extract_index_list([1], [1], []), [])

    def test_corner_case_3(self):
        self.assertListEqual(extract_index_list([1, 1], [], [1]), [])
