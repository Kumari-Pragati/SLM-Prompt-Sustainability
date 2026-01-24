import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_multiple_spaces('Hello   World'), 'Hello World')

    def test_edge_case(self):
        self.assertEqual(remove_multiple_spaces('   Hello World   '), 'Hello World')

    def test_single_space_case(self):
        self.assertEqual(remove_multiple_spaces('Hello World'), 'Hello World')

    def test_no_space_case(self):
        self.assertEqual(remove_multiple_spaces('HelloWorld'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(123)
