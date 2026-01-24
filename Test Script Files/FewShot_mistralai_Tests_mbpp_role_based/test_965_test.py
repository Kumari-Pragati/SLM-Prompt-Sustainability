import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_simple_camel_case(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MixedCase'), 'mixed_case')

    def test_uppercase(self):
        self.assertEqual(camel_to_snake('UPPERCASE'), 'upper_case')

    def test_lowercase(self):
        self.assertEqual(camel_to_snake('lowercase'), 'lower_case')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_single_letter(self):
        self.assertEqual(camel_to_snake('A'), '_a')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            camel_to_snake(123)
