import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(decode_list([[1, 2], [3, 4]]), [(2, [0, 1]), (4, [0, 1])])

    def test_edge_case_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(decode_list([[1, 2]]), [(2, [0])])

    def test_edge_case_single_element_non_list(self):
        self.assertEqual(decode_list([1]), [(1, [0])])

    def test_edge_case_single_element_list_with_non_list(self):
        self.assertEqual(decode_list([1, [2, 3]]), [(2, [0]), (3, [0])])

    def test_edge_case_multiple_non_list_elements(self):
        self.assertEqual(decode_list([1, 2, 3]), [(1, [0]), (2, [0]), (3, [0])])

    def test_edge_case_multiple_non_list_elements_with_list(self):
        self.assertEqual(decode_list([1, [2, 3], 4]), [(2, [0]), (3, [0]), (4, [0])])

    def test_edge_case_list_with_non_list_and_list(self):
        self.assertEqual(decode_list([1, [2, 3], [4, 5]]), [(2, [0]), (3, [0]), (4, [0, 1]), (5, [0, 1])])
