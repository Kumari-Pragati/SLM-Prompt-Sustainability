import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_whitespaces(""), "")

    def test_single_space(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_multiple_spaces(self):
        self.assertEqual(remove_whitespaces("Hello   World"), "HelloWorld")

    def test_tabs_and_spaces(self):
        self.assertEqual(remove_whitespaces("Hello\tWorld"), "HelloWorld")

    def test_newlines_and_spaces(self):
        self.assertEqual(remove_whitespaces("Hello\nWorld"), "HelloWorld")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_whitespaces(123)
