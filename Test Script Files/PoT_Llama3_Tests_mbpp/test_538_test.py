import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(string_list_to_tuple(['hello', 'world']), ('hello', 'world'))

    def test_edge_case_empty_list(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_edge_case_single_element(self):
        self.assertEqual(string_list_to_tuple(['hello']), ('hello',))

    def test_edge_case_single_space(self):
        self.assertEqual(string_list_to_tuple(['hello','']), ('hello',))

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(string_list_to_tuple(['hello','', 'world']), ('hello', 'world'))

    def test_edge_case_multiple_spaces_and_empty(self):
        self.assertEqual(string_list_to_tuple(['hello','', '', 'world']), ('hello', 'world'))

    def test_edge_case_multiple_spaces_and_empty_and_single(self):
        self.assertEqual(string_list_to_tuple(['hello','', '', 'world', '']), ('hello', 'world'))

    def test_edge_case_multiple_spaces_and_empty_and_single_and_empty(self):
        self.assertEqual(string_list_to_tuple(['hello','', '', 'world', '', '']), ('hello', 'world'))
