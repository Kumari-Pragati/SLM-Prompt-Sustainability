import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_single_word(self):
        self.assertEqual(snake_to_camel('python'), 'Python')

    def test_all_lowercase(self):
        self.assertEqual(snake_to_camel('lowercase_words'), 'LowercaseWords')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_single_underscore(self):
        self.assertEqual(snake_to_camel('_underscore'), 'Underscore')

    def test_no_underscore(self):
        self.assertEqual(snake_to_camel('noword'), 'Noword')

    def test_multiple_underscores(self):
        self.assertEqual(snake_to_camel('multiple__underscores'), 'MultipleUnderscores')

    def test_leading_underscore(self):
        self.assertEqual(snake_to_camel('_leading'), 'Leading')

    def test_trailing_underscore(self):
        self.assertEqual(snake_to_camel('trailing_'), 'Trailing')

    def test_all_uppercase(self):
        self.assertEqual(snake_to_camel('ALL_UPPERCASE'), 'AllUppercase')

    def test_mixed_case(self):
        self.assertEqual(snake_to_camel('MiXeD_CaSe'), 'MixedCase')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            snake_to_camel(1234)
