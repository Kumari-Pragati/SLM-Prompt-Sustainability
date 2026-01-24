import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(is_upper('hello'), 'HELLO')

    def test_empty_string(self):
        self.assertEqual(is_upper(''), '')

    def test_already_upper_case(self):
        self.assertEqual(is_upper('HELLO'), 'HELLO')

    def test_special_characters(self):
        self.assertEqual(is_upper('hello!@#'), 'HELLO!@#')

    def test_numbers(self):
        self.assertEqual(is_upper('hello123'), 'HELLO123')

    def test_whitespace(self):
        self.assertEqual(is_upper('hello world'), 'HELLO WORLD')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_upper(123)
