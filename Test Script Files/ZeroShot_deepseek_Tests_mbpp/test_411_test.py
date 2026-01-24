import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(snake_to_camel('hello'), 'Hello')

    def test_multiple_words(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_all_lowercase(self):
        self.assertEqual(snake_to_camel('lowercase'), 'Lowercase')

    def test_all_uppercase(self):
        self.assertEqual(snake_to_camel('UPPERCASE'), 'Uppercase')

    def test_mixed_case(self):
        self.assertEqual(snake_to_camel('MiXeD_CaSe'), 'MixedCase')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_string_with_numbers(self):
        self.assertEqual(snake_to_camel('string_with_123'), 'StringWith123')

    def test_string_with_special_characters(self):
        self.assertEqual(snake_to_camel('str!ng_w_spe$ch@l#chr$'), 'Str!ngWSpe$ch@l#chr$')
