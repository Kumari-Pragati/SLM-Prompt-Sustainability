import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry']), (9, 'cherry'))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_length(['hello']), (5, 'hello'))

    def test_edge_case_multiple_element_list(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry', 'date']), (7, 'cherry'))

    def test_edge_case_max_length_and_max_list_are_same(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry', 'date', 'elder']), (7, 'elder'))

    def test_edge_case_max_length_and_max_list_are_not_same(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry', 'date', 'elder', 'fig']), (4, 'apple'))

    def test_edge_case_max_length_and_max_list_are_not_same_and_max_list_is_empty(self):
        self.assertEqual(max_length(['apple', 'banana', 'cherry', 'date', 'elder', 'fig', '']), (7, 'elder'))
