import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(long_words(5, ""), [])

    def test_single_word(self):
        self.assertListEqual(long_words(3, "short word"), ["short"])

    def test_multiple_words(self):
        self.assertListEqual(long_words(4, "long word short sentence"), ["long", "sentence"])

    def test_long_word_at_beginning(self):
        self.assertListEqual(long_words(5, "longword short sentence"), ["longword"])

    def test_long_word_at_end(self):
        self.assertListEqual(long_words(5, "short sentence longword"), ["longword"])

    def test_long_word_in_middle(self):
        self.assertListEqual(long_words(5, "short longword sentence"), ["longword"])

    def test_long_word_equal_n(self):
        self.assertListEqual(long_words(5, "wordswithfiveletters"), ["wordswithfiveletters"])

    def test_long_word_just_under_n(self):
        self.assertListEqual(long_words(6, "wordswithfivelettersandanother"), [])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            long_words(5, 123)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            long_words(-1, "longword short sentence")
