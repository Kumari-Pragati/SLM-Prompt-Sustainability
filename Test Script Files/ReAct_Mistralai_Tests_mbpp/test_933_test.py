import unittest
from mbpp_933_code import camel_to_snake

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

    def test_number_at_beginning_of_camel_case(self):
        self.assertEqual(camel_to_snake('1CamelCase'), '_1_camel_case')

    def test_number_at_end_of_camel_case(self):
        self.assertEqual(camel_to_snake('CamelCase1'), 'camel_case_1')

    def test_number_in_middle_of_camel_case(self):
        self.assertEqual(camel_to_snake('Camel2Case'), 'camel_2_case')

    def test_uppercase_letters_in_camel_case(self):
        self.assertEqual(camel_to_snake('CAMELCase'), 'camel_case')

    def test_multiple_uppercase_letters_in_camel_case(self):
        self.assertEqual(camel_to_snake('PascalCase'), 'pascal_case')

    def test_special_characters_in_camel_case(self):
        self.assertEqual(camel_to_snake('CamelWithSpecial_Case'), 'camel_with_special_case')

    def test_special_characters_at_beginning_of_camel_case(self):
        self.assertEqual(camel_to_snake('SpecialCamelCase'), '_special_camel_case')

    def test_special_characters_at_end_of_camel_case(self):
        self.assertEqual(camel_to_snake('CamelCaseSpecial'), 'camel_case_special')

    def test_special_characters_in_middle_of_camel_case(self):
        self.assertEqual(camel_to_snake('CamelWithSpecialCase'), 'camel_with_special_case')

    def test_empty_string_raises_exception(self):
        with self.assertRaises(ValueError):
            camel_to_snake(None)

    def test_none_raises_exception(self):
        with self.assertRaises(TypeError):
            camel_to_snake(None)
