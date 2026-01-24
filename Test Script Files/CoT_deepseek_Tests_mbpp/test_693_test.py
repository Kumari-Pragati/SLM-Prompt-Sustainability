import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_multiple_spaces('Hello   World'), 'Hello World')

    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces('Hello World'), 'Hello World')

    def test_no_spaces(self):
        self.assertEqual(remove_multiple_spaces('HelloWorld'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_multiple_spaces_between_words(self):
        self.assertEqual(remove_multiple_spaces('Hello     World     Hello'), 'Hello World Hello')

    def test_spaces_at_start_and_end(self):
        self.assertEqual(remove_multiple_spaces('   Hello World   '), 'Hello World')

    def test_spaces_in_the_middle(self):
        self.assertEqual(remove_multiple_spaces('Hello   World'), 'Hello World')

    def test_spaces_in_the_middle_and_end(self):
        self.assertEqual(remove_multiple_spaces('Hello   World   '), 'Hello World')

    def test_spaces_in_the_middle_and_start(self):
        self.assertEqual(remove_multiple_spaces('   Hello   World'), 'Hello World')

    def test_spaces_in_the_middle_and_start_and_end(self):
        self.assertEqual(remove_multiple_spaces('   Hello   World   '), 'Hello World')
