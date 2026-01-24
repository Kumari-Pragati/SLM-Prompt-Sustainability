import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_multiple_spaces('Hello   World'), 'Hello World')

    def test_single_space_case(self):
        self.assertEqual(remove_multiple_spaces('Hello World'), 'Hello World')

    def test_no_spaces_case(self):
        self.assertEqual(remove_multiple_spaces('HelloWorld'), 'HelloWorld')

    def test_empty_string_case(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_multiple_spaces_between_words(self):
        self.assertEqual(remove_multiple_spaces('Hello     World     Hello'), 'Hello World Hello')

    def test_spaces_at_start_and_end(self):
        self.assertEqual(remove_multiple_spaces('   Hello   World   '), 'Hello World')

    def test_spaces_only_string(self):
        self.assertEqual(remove_multiple_spaces('   '), ' ')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(None)
