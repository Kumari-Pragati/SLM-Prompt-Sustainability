import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('CamelCase'), 'camel_case')

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake('ThisIsCamelCase'), 'this_is_camel_case')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MixedCase'), 'mixed_case')

    def test_numbers_in_camel_case(self):
        self.assertEqual(camel_to_snake('3CamelCase'), '3_camel_case')

    def test_special_characters_in_camel_case(self):
        self.assertEqual(camel_to_snake('CamelCaseWithSpecialCharacters!'), 'camel_case_with_special_characters_')

    def test_invalid_input(self):
        self.assertRaises(TypeError, camel_to_snake, 123)
        self.assertRaises(TypeError, camel_to_snake, [1, 2, 3])
        self.assertRaises(TypeError, camel_to_snake, (1, 2, 3))
        self.assertRaises(TypeError, camel_to_snake, None)
        self.assertRaises(TypeError, camel_to_snake, False)
        self.assertRaises(TypeError, camel_to_snake, True)
