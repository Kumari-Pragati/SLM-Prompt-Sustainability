import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_Char('hello', 'l'), 'heo')

    def test_edge_condition_empty_string(self):
        self.assertEqual(remove_Char('', 'a'), '')

    def test_edge_condition_char_not_in_string(self):
        self.assertEqual(remove_Char('hello', 'z'), 'hello')

    def test_boundary_condition_single_char_in_string(self):
        self.assertEqual(remove_Char('a', 'a'), '')

    def test_boundary_condition_multiple_chars_in_string(self):
        self.assertEqual(remove_Char('aaaa', 'a'), '')

    def test_complex_case_multiple_chars_to_remove(self):
        self.assertEqual(remove_Char('hello world', 'l'), 'heo word ')

    def test_complex_case_char_present_multiple_times(self):
        self.assertEqual(remove_Char('mississippi', 's'), 'mippi')
