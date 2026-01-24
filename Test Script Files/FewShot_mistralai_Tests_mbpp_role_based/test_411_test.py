import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(snake_to_camel('some_variable_name'), 'someVariableName')

    def test_edge_case_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_edge_case_single_word(self):
        self.assertEqual(snake_to_camel('variable'), 'variable')

    def test_edge_case_single_uppercase_word(self):
        self.assertEqual(snake_to_camel('Variable'), 'Variable')

    def test_edge_case_single_lowercase_word(self):
        self.assertEqual(snake_to_camel('variable'), 'variable')

    def test_edge_case_multiple_words_with_underscores(self):
        self.assertEqual(snake_to_camel('some_variable_name'), 'someVariableName')

    def test_edge_case_multiple_words_with_leading_underscore(self):
        self.assertEqual(snake_to_camel('_some_variable_name'), 'someVariableName')

    def test_edge_case_multiple_words_with_trailing_underscore(self):
        self.assertEqual(snake_to_camel('some_variable_name_'), 'someVariableName')

    def test_edge_case_multiple_words_with_leading_and_trailing_underscores(self):
        self.assertEqual(snake_to_camel('_some_variable_name_'), 'someVariableName')

    def test_edge_case_multiple_words_with_only_leading_underscores(self):
        self.assertEqual(snake_to_camel('__some_variable_name__'), 'someVariableName')

    def test_edge_case_multiple_words_with_only_trailing_underscores(self):
        self.assertEqual(snake_to_camel('some_variable_name__'), 'someVariableName')

    def test_edge_case_multiple_words_with_leading_and_trailing_underscores(self):
        self.assertEqual(snake_to_camel('__some_variable_name__'), 'someVariableName')

    def test_edge_case_multiple_words_with_only_uppercase_letters(self):
        self.assertEqual(snake_to_camel('SOME_VARIABLE_NAME'), 'someVariableName')

    def test_edge_case_multiple_words_with_only_lowercase_letters(self):
        self.assertEqual(snake_to_camel('some_variable_name'), 'someVariableName')

    def test_edge_case_multiple_words_with_mixed_case(self):
        self.assertEqual(snake_to_camel('Some_Variable_Name'), 'someVariableName')

    def test_edge_case_multiple_words_with_numbers(self):
        self.assertEqual(snake_to_camel('some_variable_123_name'), 'someVariable123Name')

    def test_edge_case_multiple_words_with_special_characters(self):
        self.assertEqual(snake_to_camel('some_variable_#$%^&*_name'), 'someVariable#$%^&*Name')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            snake_to_camel(123)
