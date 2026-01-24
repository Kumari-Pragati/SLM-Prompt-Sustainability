import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_extra_char('Hello, World!'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_extra_char(''), '')

    def test_string_with_numbers(self):
        self.assertEqual(remove_extra_char('1234567890'), '1234567890')

    def test_string_with_special_chars(self):
        self.assertEqual(remove_extra_char('!@#$%^&*()'), '')

    def test_string_with_spaces(self):
        self.assertEqual(remove_extra_char('Hello World'), 'HelloWorld')

    def test_string_with_mixed_case(self):
        self.assertEqual(remove_extra_char('Hello WoRlD!'), 'HelloWoRlD')

    def test_string_with_underscore(self):
        self.assertEqual(remove_extra_char('Hello_World'), 'HelloWorld')

    def test_string_with_multiple_underscores(self):
        self.assertEqual(remove_extra_char('Hello___World'), 'HelloWorld')

    def test_string_with_multiple_special_chars(self):
        self.assertEqual(remove_extra_char('Hello!!!World'), 'HelloWorld')

    def test_string_with_multiple_spaces(self):
        self.assertEqual(remove_extra_char('Hello   World'), 'HelloWorld')
