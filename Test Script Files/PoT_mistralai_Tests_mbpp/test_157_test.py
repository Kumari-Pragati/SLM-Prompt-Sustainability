import unittest
from mbpp_157_code import islice, chain

from157_code import encode_list

class TestEncodeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(encode_list([1, 1, 2, 3, 1, 2, 1, 1]),
                         [[1, 1], [2, 2], [1, 3], [1, 1], [1, 2], [4, 1]])

    def test_edge_case_single_element(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_edge_case_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_corner_case_duplicate_start_and_end(self):
        self.assertEqual(encode_list([1, 1, 2, 1, 1]),
                         [[1, 1], [1, 2], [1, 1]])

    def test_corner_case_duplicate_start_and_end_with_single_element(self):
        self.assertEqual(encode_list([1, 1]), [[1, 1], [1, 1]])

    def test_corner_case_duplicate_start_and_end_with_single_element_edge(self):
        self.assertEqual(encode_list([1]), [[1, 1]])
