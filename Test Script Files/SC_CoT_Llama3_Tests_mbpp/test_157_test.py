import unittest
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(encode_list([1, 2, 2, 3, 3, 3, 4, 5, 5]), [[2, 1], [2, 2], [3, 3], [1, 4], [2, 5]])

    def test_edge_case_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(encode_list([1, 1, 1]), [[3, 1]])

    def test_edge_case_all_duplicates(self):
        self.assertEqual(encode_list([1, 1, 1, 1, 1]), [[5, 1]])

    def test_edge_case_all_unique(self):
        self.assertEqual(encode_list([1, 2, 3, 4, 5]), [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            encode_list("test")
