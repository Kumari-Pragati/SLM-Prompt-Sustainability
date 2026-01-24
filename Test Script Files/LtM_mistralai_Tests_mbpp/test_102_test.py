import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(snake_to_camel('some_word'), 'someWord')
        self.assertEqual(snake_to_camel('another_word'), 'anotherWord')

    def test_edge_input(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('word_'), 'word')
        self.assertEqual(snake_to_camel('word__'), 'word')
        self.assertEqual(snake_to_camel('word_word'), 'wordWord')

    def test_complex_input(self):
        self.assertEqual(snake_to_camel('a_very_long_word'), 'aVeryLongWord')
        self.assertEqual(snake_to_camel('a_123_word'), 'a123Word')
        self.assertEqual(snake_to_camel('a_word_123'), 'aWord123')
        self.assertEqual(snake_to_camel('123_word'), '123Word')
        self.assertEqual(snake_to_camel('word_1A'), 'word1A')
