import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_extra_char('Hello, World!'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_extra_char(''), '')

    def test_string_with_no_extra_chars(self):
        self.assertEqual(remove_extra_char('PythonProgramming'), 'PythonProgramming')

    def test_string_with_only_extra_chars(self):
        self.assertEqual(remove_extra_char('     ,,,,!!!'), '')

    def test_string_with_mixed_chars(self):
        self.assertEqual(remove_extra_char('P@#y!th0nPr0gr@m@!n@g'), 'PythonProgramming')

    def test_string_with_special_chars(self):
        self.assertEqual(remove_extra_char('Hello, World!'), 'HelloWorld')

    def test_string_with_special_chars_and_spaces(self):
        self.assertEqual(remove_extra_char('H  e  l  l  o  ,  W  o  r  l  d  !'), 'HelloWorld')
