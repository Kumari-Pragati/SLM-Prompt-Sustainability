import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_Char('hello', 'l'), 'heo')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_Char('', 'a'), '')

    def test_boundary_case_single_character(self):
        self.assertEqual(remove_Char('a', 'a'), '')

    def test_boundary_case_repeated_character(self):
        self.assertEqual(remove_Char('aaaa', 'a'), '')

    def test_error_handling_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_Char(123, 'a')

    def test_error_handling_non_character_removal(self):
        with self.assertRaises(ValueError):
            remove_Char('hello', 'z')
