import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "HeWorlD")
        self.assertEqual(capitalize_first_last_letters("hello"), "HeLlO")
        self.assertEqual(capitalize_first_last_letters("world"), "WoRlD")

    def test_empty_input(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_single_word(self):
        self.assertEqual(capitalize_first_last_letters("hello"), "HeLlO")

    def test_multiple_words(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "HeWorlD")
        self.assertEqual(capitalize_first_last_letters("hello world again"), "HeWoRlD AgAiN")

    def test_long_string(self):
        self.assertEqual(capitalize_first_last_letters("hello world again this is a test"), "HeWoRlD AgAiN ThIs Is A TeSt")

    def test_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("hello, world!"), "HeWorlD, WoRlD!")

    def test_numbers(self):
        self.assertEqual(capitalize_first_last_letters("hello 123 world"), "HeWoRlD 123 WoRlD")
