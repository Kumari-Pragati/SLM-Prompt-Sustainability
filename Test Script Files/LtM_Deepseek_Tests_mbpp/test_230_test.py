import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(replace_blank('Hello World', '_'), 'Hello_World')

    def test_empty_string(self):
        self.assertEqual(replace_blank('', '_'), '')

    def test_string_with_no_spaces(self):
        self.assertEqual(replace_blank('HelloWorld', '_'), 'HelloWorld')

    def test_string_with_multiple_spaces(self):
        self.assertEqual(replace_blank('Hello   World', '_'), 'Hello_World')

    def test_special_char_as_replacement(self):
        self.assertEqual(replace_blank('Hello World', ''), 'HelloWorld')

    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(replace_blank(' Hello World ', '_'), '_Hello_World_')
