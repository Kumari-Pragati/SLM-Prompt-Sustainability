import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_length_list([1, 2, 3, 4, 5]), (5, [5]))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_length_list([]), (0, []))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_length_list(['a']), (1, ['a']))

    def test_edge_case_single_element_list_with_empty_string(self):
        self.assertEqual(max_length_list(['', 'b']), (1, ['']))

    def test_edge_case_multiple_element_list(self):
        self.assertEqual(max_length_list(['a', 'b', 'c']), (1, ['c']))

    def test_edge_case_multiple_element_list_with_empty_string(self):
        self.assertEqual(max_length_list(['', 'a', 'b', 'c']), (1, ['c']))

    def test_edge_case_multiple_element_list_with_empty_string_and_duplicates(self):
        self.assertEqual(max_length_list(['', 'a', 'b', 'c', 'a']), (1, ['c']))

    def test_edge_case_multiple_element_list_with_empty_string_and_duplicates_and_duplicates(self):
        self.assertEqual(max_length_list(['', 'a', 'b', 'c', 'a', 'b']), (1, ['c']))
