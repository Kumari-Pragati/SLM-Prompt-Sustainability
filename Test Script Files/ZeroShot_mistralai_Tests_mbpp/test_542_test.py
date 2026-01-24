import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(fill_spaces(""), "")

    def test_single_word(self):
        self.assertEqual(fill_spaces("hello"), "hello")
        self.assertEqual(fill_spaces("world"), "world")

    def test_multiple_words(self):
        self.assertEqual(fill_spaces("hello world"), "hello:world")
        self.assertEqual(fill_spaces("apple banana"), "apple:banana")

    def test_punctuation_at_start_and_end(self):
        self.assertEqual(fill_spaces(".,!"), ":.,!")
        self.assertEqual(fill_spaces(";:?"), ":;:?")

    def test_punctuation_in_middle(self):
        self.assertEqual(fill_spaces("hello, world."), "hello:world.")
        self.assertEqual(fill_spaces("apple; banana!"), "apple:banana!")

    def test_multiple_punctuation(self):
        self.assertEqual(fill_spaces("hello, world.!?"), "hello:world.!?")
        self.assertEqual(fill_spaces("apple; banana; car!?"), "apple:banana:car!?")

    def test_spaces_only(self):
        self.assertEqual(fill_spaces("   "), ":")
