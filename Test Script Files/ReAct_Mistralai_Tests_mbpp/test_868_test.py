import unittest
from mbpp_868_code import length_OfLastWord

class TestLengthOfLastWord(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(length_OfLastWord(""), 0)

    def test_single_word(self):
        self.assertEqual(length_OfLastWord("hello"), 5)

    def test_multiple_words_with_space(self):
        self.assertEqual(length_OfLastWord("hello world"), 5)

    def test_multiple_words_without_space(self):
        self.assertEqual(length_OfLastWord("helloworld"), 7)

    def test_leading_space(self):
        self.assertEqual(length_OfLastWord(" world"), 0)

    def test_trailing_space(self):
        self.assertEqual(length_OfLastWord("hello "), 5)

    def test_leading_and_trailing_space(self):
        self.assertEqual(length_OfLastWord("   world   "), 5)

    def test_single_space(self):
        self.assertEqual(length_OfLastWord("hello "), 4)

    def test_multiple_spaces(self):
        self.assertEqual(length_OfLastWord("hello   world"), 5)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            length_OfLastWord(123)
