import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(len_log([[1, 2, 3], [4, 5, 6]]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(len_log([]), None)

    def test_edge_case_single_element(self):
        self.assertEqual(len_log([['a']]), 1)

    def test_edge_case_single_element_empty(self):
        self.assertEqual(len_log([[]]), None)

    def test_edge_case_single_element_single_char(self):
        self.assertEqual(len_log([['a']]), 1)

    def test_edge_case_single_element_multiple_chars(self):
        self.assertEqual(len_log([['abc']]), 3)

    def test_edge_case_multiple_elements(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f']]), 3)

    def test_edge_case_multiple_elements_empty(self):
        self.assertEqual(len_log([[], ['d', 'e', 'f']]), 3)

    def test_edge_case_multiple_elements_single_char(self):
        self.assertEqual(len_log([['a'], ['b']]), 1)

    def test_edge_case_multiple_elements_multiple_chars(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f']]), 3)

    def test_edge_case_multiple_elements_empty_and_single_char(self):
        self.assertEqual(len_log([[], ['a']]), 1)

    def test_edge_case_multiple_elements_empty_and_multiple_chars(self):
        self.assertEqual(len_log([[], ['a', 'b', 'c']]), 3)

    def test_edge_case_multiple_elements_single_char_and_multiple_chars(self):
        self.assertEqual(len_log([['a'], ['b', 'c']]), 1)

    def test_edge_case_multiple_elements_single_char_and_empty(self):
        self.assertEqual(len_log([['a'], []]), 1)

    def test_edge_case_multiple_elements_multiple_chars_and_empty(self):
        self.assertEqual(len_log([['a', 'b', 'c'], []]), 3)

    def test_edge_case_multiple_elements_multiple_chars_and_single_char(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d']]), 3)

    def test_edge_case_multiple_elements_multiple_chars_and_multiple_chars(self):
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f']]), 3)
