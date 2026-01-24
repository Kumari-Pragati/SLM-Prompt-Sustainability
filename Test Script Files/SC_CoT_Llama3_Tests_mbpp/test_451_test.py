import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_multiple_spaces(self):
        self.assertEqual(remove_whitespaces("   Hello   World   "), "HelloWorld")

    def test_single_space(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_multiple_lines(self):
        self.assertEqual(remove_whitespaces("Hello\nWorld"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_whitespaces(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_whitespaces(" "), "")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_whitespaces("   "), "")

    def test_edge_case_newline(self):
        self.assertEqual(remove_whitespaces("\n"), "")

    def test_edge_case_tab(self):
        self.assertEqual(remove_whitespaces("\t"), "")

    def test_edge_case_carriage_return(self):
        self.assertEqual(remove_whitespaces("\r"), "")

    def test_edge_case_mixed_spaces(self):
        self.assertEqual(remove_whitespaces("Hello   World\n"), "HelloWorld")

    def test_edge_case_mixed_spaces_newline(self):
        self.assertEqual(remove_whitespaces("Hello   World\n   "), "HelloWorld")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_whitespaces(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_whitespaces(None)
