import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_spaces('Hello World'), 'Hello World')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('Hello   World'), 'Hello World')

    def test_trailing_spaces(self):
        self.assertEqual(remove_spaces('Hello World   '), 'Hello World')

    def test_single_space(self):
        self.assertEqual(remove_spaces('Hello World'), 'Hello World')

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_special_characters(self):
        self.assertEqual(remove_spaces('Hello@World'), 'Hello@World')

    def test_numbers(self):
        self.assertEqual(remove_spaces('Hello123World456'), 'Hello123World456')

    def test_special_case(self):
        self.assertEqual(remove_spaces('  Hello   World  '), 'Hello World')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_spaces(12345)
