import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_spaces('Hello World'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces('HelloWorld'), 'HelloWorld')

    def test_string_with_multiple_spaces(self):
        self.assertEqual(remove_spaces('Hello   World'), 'HelloWorld')

    def test_string_with_special_characters(self):
        self.assertEqual(remove_spaces('Hello@World'), 'Hello@World')

    def test_string_with_numbers(self):
        self.assertEqual(remove_spaces('Hello123World'), 'Hello123World')

    def test_string_with_mixed_case(self):
        self.assertEqual(remove_spaces('Hello WoRlD'), 'HelloWoRlD')
