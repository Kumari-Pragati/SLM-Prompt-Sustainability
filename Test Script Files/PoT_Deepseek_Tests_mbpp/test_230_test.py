import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_blank('Hello World', '_'), 'Hello_World')

    def test_empty_string(self):
        self.assertEqual(replace_blank('', '_'), '')

    def test_no_blanks(self):
        self.assertEqual(replace_blank('HelloWorld', '_'), 'HelloWorld')

    def test_single_blank(self):
        self.assertEqual(replace_blank('Hello World', '_'), 'Hello_World')

    def test_multiple_blanks(self):
        self.assertEqual(replace_blank('Hello  World  ', '_'), 'Hello__World_')

    def test_special_char(self):
        self.assertEqual(replace_blank('Hello World', '#'), 'Hello#World')

    def test_numeric_char(self):
        self.assertEqual(replace_blank('123 456', '0'), '1230456')

    def test_whitespace_char(self):
        self.assertEqual(replace_blank('Hello World', ' '), 'Hello World')
