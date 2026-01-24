import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry']), (9, 'cherry'))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_length(['hello']), (5, 'hello'))

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(max_length(['hello', 'world']), (5, 'hello'))

    def test_edge_case_longest_string(self):
        self.assertEqual(max_length(['hello', 'world', 'abcdefghijklmnopqrstuvwxyz']), (26, 'abcdefghijklmnopqrstuvwxyz'))

    def test_edge_case_tie(self):
        self.assertEqual(max_length(['hello', 'world', 'abc']), (3, 'abc'))

    def test_edge_case_empty_string(self):
        self.assertEqual(max_length(['', 'hello']), (5, 'hello'))

    def test_edge_case_single_empty_string(self):
        self.assertEqual(max_length(['']), (0, None))

    def test_edge_case_multiple_empty_strings(self):
        self.assertEqual(max_length(['', '', '']), (0, None))
