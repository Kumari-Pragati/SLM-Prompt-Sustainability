import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_length("Hello World", 5), "Hello World")

    def test_single_word(self):
        self.assertEqual(remove_length("Hello", 3), "Hello")

    def test_multiple_words(self):
        self.assertEqual(remove_length("Hello World Foo", 3), "Hello World Foo")

    def test_empty_string(self):
        self.assertEqual(remove_length("", 5), "")

    def test_single_word_of_length_K(self):
        self.assertEqual(remove_length("Hello", 5), "")

    def test_multiple_words_of_length_K(self):
        self.assertEqual(remove_length("Hello World Foo", 5), "Hello World Foo")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_length(123, 5)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            remove_length("Hello", "five")
