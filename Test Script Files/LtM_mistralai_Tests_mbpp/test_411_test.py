import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(snake_to_camel('some_word'), 'someWord')
        self.assertEqual(snake_to_camel('single_word'), 'singleWord')
        self.assertEqual(snake_to_camel('no_underscores'), 'noUnderscores')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('__'), '__')
        self.assertEqual(snake_to_camel('word_'), 'word')
        self.assertEqual(snake_to_camel('word_with_number_123'), 'wordWithNumber123')

    def test_complex_input(self):
        self.assertEqual(snake_to_camel('this_is_a_test'), 'thisIsATest')
        self.assertEqual(snake_to_camel('this_is_a_very_long_test'), 'thisIsAVeryLongTest')
        self.assertEqual(snake_to_camel('this_is_a_test_with_numbers_123_and_symbols_#$%^&*()'), 'thisIsATestWithNumbers123AndSymbols#$%^&*')
