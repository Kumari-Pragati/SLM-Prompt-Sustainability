import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MixedCase'), 'mixed_case')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_single_uppercase_letter(self):
        self.assertEqual(camel_to_snake('UpperCase'), '_upper_case')

    def test_single_lowercase_letter(self):
        self.assertEqual(camel_to_snake('lowerCase'), 'lower_case')

    def test_uppercase_and_lowercase(self):
        self.assertEqual(camel_to_snake('UpperLower'), '_upper_lower')

    def test_numbers_in_camel_case(self):
        self.assertEqual(camel_to_snake('CamelNumber'), 'camel_number')

    def test_numbers_at_start_and_end(self):
        self.assertEqual(camel_to_snake('1CamelNumber2'), '1_camel_number_2')

    def test_numbers_in_middle(self):
        self.assertEqual(camel_to_snake('CamelNumberMiddle'), 'camel_number_middle')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            camel_to_snake(123)
