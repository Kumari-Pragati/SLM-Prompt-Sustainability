import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(""), "")

    def test_single_word(self):
        self.assertEqual(camel_to_snake("hello"), "hello")

    def test_camel_case(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake("helloWorldThisIsATest"), "hello_world_this_is_a_test")

    def test_numbers(self):
        self.assertEqual(camel_to_snake("hello123World"), "hello_123_world")

    def test_punctuation(self):
        self.assertEqual(camel_to_snake("hello!World"), "hello_world")

    def test_non_ascii_characters(self):
        self.assertEqual(camel_to_snake("hëlloWorld"), "hëllo_world")
