import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake('PascalCase'), 'pascal_case')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MixedCase'), 'mixed_case')

    def test_number_in_camel_case(self):
        self.assertEqual(camel_to_snake('Camel1Case'), 'camel_1_case')

    def test_number_at_start_of_camel_case(self):
        self.assertEqual(camel_to_snake('1CamelCase'), '_1_camel_case')

    def test_number_at_end_of_camel_case(self):
        self.assertEqual(camel_to_snake('CamelCase1'), 'camel_case_1')

    def test_number_in_middle_of_camel_case(self):
        self.assertEqual(camel_to_snake('Camel2Case'), 'camel_2_case')

    def test_uppercase_letters_in_camel_case(self):
        self.assertEqual(camel_to_snake('UPPERCASE'), '_upper_case')

    def test_leading_underscore_in_camel_case(self):
        self.assertEqual(camel_to_snake('_CamelCase'), '_camel_case')

    def test_trailing_underscore_in_camel_case(self):
        self.assertEqual(camel_to_snake('CamelCase_'), 'camel_case')

    def test_leading_and_trailing_underscores_in_camel_case(self):
        self.assertEqual(camel_to_snake('__CamelCase__'), '_camel_case')

    def test_multiple_consecutive_underscores_in_camel_case(self):
        self.assertEqual(camel_to_snake('___CamelCase___'), '_camel_case')

    def test_non_alphanumeric_characters_in_camel_case(self):
        self.assertEqual(camel_to_snake('Camel!Case'), 'camel_case')

    def test_invalid_regex_pattern(self):
        with self.assertRaises(re.error):
            camel_to_snake('InvalidPattern')
