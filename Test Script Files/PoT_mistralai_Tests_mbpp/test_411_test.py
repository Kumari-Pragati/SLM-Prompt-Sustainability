import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(snake_to_camel('this_is_a_test'), 'thisIsATest')
        self.assertEqual(snake_to_camel('another_test'), 'anotherTest')
        self.assertEqual(snake_to_camel('single_word'), 'singleWord')
        self.assertEqual(snake_to_camel(''), '')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('__'), '__')
        self.assertEqual(snake_to_camel('_word'), 'Word')
        self.assertEqual(snake_to_camel('word_'), 'Word')
        self.assertEqual(snake_to_camel('word_with_numbers_123'), 'wordWithNumbers123')

    def test_corner_cases(self):
        self.assertEqual(snake_to_camel('word_with_special_characters!@#$%^&*()'), 'wordWithSpecialCharacters!@#$%^&*')
        self.assertEqual(snake_to_camel('word_with_multiple_consecutive_underscores___'), 'WordWithMultipleConsecutiveUnderscores')
