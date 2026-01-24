import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_spaces('Hello World'), 'Hello World')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('Hello   World'), 'Hello World')

    def test_single_space(self):
        self.assertEqual(remove_spaces('Hello World'), 'Hello World')

    def test_no_spaces(self):
        self.assertEqual(remove_spaces('HelloWorld'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_large_spaces(self):
        self.assertEqual(remove_spaces('Hello        World'), 'Hello World')

    def test_spaces_at_ends(self):
        self.assertEqual(remove_spaces(' Hello World '), 'Hello World')

    def test_special_characters(self):
        self.assertEqual(remove_spaces('Hello, World!'), 'Hello, World!')

    def test_numbers_with_spaces(self):
        self.assertEqual(remove_spaces('1 2 3 4'), '1 2 3 4')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_spaces(1234)
