import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_blank('Hello World', '_'), 'Hello_World')

    def test_empty_string(self):
        self.assertEqual(replace_blank('', '_'), '')

    def test_no_blanks(self):
        self.assertEqual(replace_blank('HelloWorld', '_'), 'HelloWorld')

    def test_special_character(self):
        self.assertEqual(replace_blank('Hello World', '#'), 'Hello#World')

    def test_multiple_blanks(self):
        self.assertEqual(replace_blank('Hello   World', '_'), 'Hello__World')

    def test_whitespace_characters(self):
        self.assertEqual(replace_blank('Hello\tWorld', '_'), 'Hello_World')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            replace_blank(None, '_')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            replace_blank(12345, '_')

    def test_empty_char_input(self):
        self.assertEqual(replace_blank('Hello World', ''), 'Hello World')
