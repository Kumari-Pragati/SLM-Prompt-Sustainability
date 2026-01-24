import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(most_occurrences(['hello world', 'world hello']), 'hello')

    # Test for edge and boundary conditions
    def test_empty_input(self):
        self.assertEqual(most_occurrences([]), '')

    def test_single_word_input(self):
        self.assertEqual(most_occurrences(['hello']), 'hello')

    # Test for more complex or corner cases
    def test_same_frequency_words(self):
        self.assertEqual(most_occurrences(['hello hello', 'world world']), 'hello')

    def test_multiple_words_with_same_frequency(self):
        self.assertEqual(most_occurrences(['hello world', 'world hello']), 'hello')

    def test_special_characters(self):
        self.assertEqual(most_occurrences(['hello! world', 'world hello']), 'hello')

    # Test for invalid inputs
    def test_none_input(self):
        with self.assertRaises(TypeError):
            most_occurrences(None)

    def test_integer_input(self):
        with self.assertRaises(TypeError):
            most_occurrences(123)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            most_occurrences(123.45)
