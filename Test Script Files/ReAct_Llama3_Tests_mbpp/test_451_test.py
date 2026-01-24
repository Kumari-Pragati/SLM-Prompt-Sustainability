import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_multiple_spaces(self):
        self.assertEqual(remove_whitespaces("Hello   World"), "HelloWorld")

    def test_single_space(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_no_spaces(self):
        self.assertEqual(remove_whitespaces("HelloWorld"), "HelloWorld")

    def test_edge_case_newline(self):
        self.assertEqual(remove_whitespaces("Hello\nWorld"), "HelloWorld")

    def test_edge_case_tab(self):
        self.assertEqual(remove_whitespaces("Hello\tWorld"), "HelloWorld")

    def test_edge_case_carriage_return(self):
        self.assertEqual(remove_whitespaces("Hello\rWorld"), "HelloWorld")

    def test_edge_case_mixed(self):
        self.assertEqual(remove_whitespaces("Hello\n\tWorld\r"), "HelloWorld")

    def test_error_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_whitespaces(123)

    def test_error_case_non_string_input2(self):
        with self.assertRaises(TypeError):
            remove_whitespaces([1, 2, 3])
