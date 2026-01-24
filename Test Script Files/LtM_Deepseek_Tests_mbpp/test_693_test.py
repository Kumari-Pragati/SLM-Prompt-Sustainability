import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(remove_multiple_spaces('Hello  World'), 'Hello World')

    # Test for edge and boundary conditions
    def test_empty_input(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_single_space_input(self):
        self.assertEqual(remove_multiple_spaces(' '), ' ')

    # Test for more complex or corner cases
    def test_multiple_spaces_between_words(self):
        self.assertEqual(remove_multiple_spaces('Hello     World'), 'Hello World')

    def test_multiple_spaces_at_end_of_string(self):
        self.assertEqual(remove_multiple_spaces('Hello   '), 'Hello ')

    def test_multiple_spaces_at_start_of_string(self):
        self.assertEqual(remove_multiple_spaces('   Hello'), ' Hello')

    def test_multiple_spaces_in_middle_of_string(self):
        self.assertEqual(remove_multiple_spaces('Hello   World'), 'Hello World')

    def test_multiple_spaces_in_empty_string(self):
        self.assertEqual(remove_multiple_spaces('   '), ' ')
