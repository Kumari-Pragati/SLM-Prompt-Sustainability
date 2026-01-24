import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(len_log([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(len_log([]), None)

    def test_edge_case_single_element_list(self):
        self.assertEqual(len_log([[1, 2, 3]]), 3)

    def test_edge_case_all_elements_of_same_length(self):
        self.assertEqual(len_log([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3)

    def test_edge_case_all_elements_of_different_lengths(self):
        self.assertEqual(len_log([[1, 2, 3], [4, 5], [7, 8, 9, 10]]), 1)

    def test_edge_case_list_with_empty_string(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f'], '']), 1)

    def test_edge_case_list_with_empty_string_and_empty_list(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f'], '']), 1)
