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
        self.assertEqual(capital_words_spaces("HeLlO wOrLd"), "HeLlO wOrLd")
        self.assertEqual(capital_words_spaces("PyThOn PrOgRaMmInG"), "PyThOn PrOgRaMmInG")
        self.assertEqual(capital_words_spaces("JavaScRiPt jAvAsCrIpT"), "JavaScRiPt jAvAsCrIpT")

    def test_punctuation(self):
        self.assertEqual(capital_words_spaces("Hello, World!"), "Hello, World!")
        self.assertEqual(capital_words_spaces("Python! Programming?"), "Python! Programming?")
        self.assertEqual(capital_words_spaces("JavaScript! JavaScript?"), "JavaScript! JavaScript?")

    def test_numbers(self):
        self.assertEqual(capital_words_spaces("123 Hello World 456"), "123 Hello World 456")
        self.assertEqual(capital_words_spaces("Hello World 12345"), "Hello World 12345")
        self.assertEqual(capital_words_spaces("Hello World 123456789"), "Hello World 123456789")

    def test_special_characters(self):
        self.assertEqual(capital_words_spaces("Hello@World#"), "Hello@World#")
        self.assertEqual(capital_words_spaces("Python$Programming%"), "Python$Programming%")
        self.assertEqual(capital_words_spaces("JavaScript^JavaScript&"), "JavaScript^JavaScript&")

    def test_multiple_spaces(self):
        self.assertEqual(capital_words_spaces(" Hello World "), " Hello World ")
        self.assertEqual(capital_words_spaces(" PyThOn PrOgRaMmInG "), " PyThOn PrOgRaMmInG ")
        self.assertEqual(capital_words_spaces(" JavaScRiPt jAvAsCrIpT "), " JavaScRiPt jAvAsCrIpT ")

    def test_empty_words(self):
        self.assertEqual(capital_words_spaces(" Hello   World  "), " Hello   World  ")
        self.assertEqual(capital_words_spaces(" PyThOn    PrOgRaMmInG   "), " PyThOn    PrOgRaMmInG   ")
        self.assertEqual(capital_words_spaces(" JavaScRiPt       jAvAsCrIpT       "), " JavaScRiPt       jAvAsCrIpT       ")
