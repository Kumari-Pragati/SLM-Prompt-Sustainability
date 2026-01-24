import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_single_word(self):
        self.assertEqual(capital_words_spaces("Hello"), "Hello")
        self.assertEqual(capital_words_spaces("World"), "World")
        self.assertEqual(capital_words_spaces("Python"), "Python")

    def test_multiple_words(self):
        self.assertEqual(capital_words_spaces("Hello World"), "Hello World")
        self.assertEqual(capital_words_spaces("Python Programming"), "Python Programming")
        self.assertEqual(capital_words_spaces("JavaScript JavaScript"), "JavaScript JavaScript")

    def test_mixed_case(self):
        self.assertEqual(capital_words_spaces("HeLlo WoRlD"), "HeLlo World")
        self.assertEqual(capital_words_spaces("PyThOn PrOgRaMmInG"), "Python Programming")
        self.assertEqual(capital_words_spaces("JavaScRiPt jAvAsCript"), "JavaScript JavaScript")

    def test_special_characters(self):
        self.assertEqual(capital_words_spaces("Hello@World"), "Hello @World")
        self.assertEqual(capital_words_spaces("Python#Programming"), "Python #Programming")
        self.assertEqual(capital_words_spaces("JavaScript$JavaScript"), "JavaScript $JavaScript")

    def test_numbers(self):
        self.assertEqual(capital_words_spaces("Hello123World"), "Hello 123 World")
        self.assertEqual(capital_words_spaces("Python456Programming"), "Python 456 Programming")
        self.assertEqual(capital_words_spaces("JavaScript789JavaScript"), "JavaScript 789 JavaScript")
