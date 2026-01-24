import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(last_occurence_char('hello', 'l'), 5)

    def test_edge_case_char_not_in_string(self):
        self.assertIsNone(last_occurence_char('hello', 'z'))

    def test_boundary_case_empty_string(self):
        self.assertIsNone(last_occurence_char('', 'a'))

    def test_boundary_case_string_with_single_char(self):
        self.assertEqual(last_occurence_char('a', 'a'), 1)

    def test_invalid_input_none_string(self):
        with self.assertRaises(TypeError):
            last_occurence_char(None, 'a')

    def test_invalid_input_none_char(self):
        with self.assertRaises(TypeError):
            last_occurence_char('hello', None)
