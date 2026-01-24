import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(long_words(5, "Hello World"), ["World"])

    def test_edge_case_n_zero(self):
        self.assertEqual(long_words(0, "Hello World"), ["Hello", "World"])

    def test_edge_case_n_one(self):
        self.assertEqual(long_words(1, "Hello World"), ["Hello", "World"])

    def test_edge_case_n_longer_than_word(self):
        self.assertEqual(long_words(10, "Hello World"), ["Hello", "World"])

    def test_edge_case_n_shorter_than_word(self):
        self.assertEqual(long_words(10, "Hello"), ["Hello"])

    def test_edge_case_empty_string(self):
        self.assertEqual(long_words(5, ""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(long_words(5, "Hello"), ["Hello"])

    def test_edge_case_single_word_n_zero(self):
        self.assertEqual(long_words(0, "Hello"), ["Hello"])

    def test_edge_case_single_word_n_one(self):
        self.assertEqual(long_words(1, "Hello"), ["Hello"])

    def test_edge_case_single_word_n_longer_than_word(self):
        self.assertEqual(long_words(10, "Hello"), ["Hello"])

    def test_edge_case_single_word_n_shorter_than_word(self):
        self.assertEqual(long_words(10, "Hello"), ["Hello"])

    def test_edge_case_single_word_n_equal_to_word(self):
        self.assertEqual(long_words(5, "Hello"), ["Hello"])

    def test_edge_case_multiple_words(self):
        self.assertEqual(long_words(5, "Hello World Foo"), ["World", "Foo"])

    def test_edge_case_multiple_words_n_zero(self):
        self.assertEqual(long_words(0, "Hello World Foo"), ["Hello", "World", "Foo"])

    def test_edge_case_multiple_words_n_one(self):
        self.assertEqual(long_words(1, "Hello World Foo"), ["Hello", "World", "Foo"])

    def test_edge_case_multiple_words_n_longer_than_word(self):
        self.assertEqual(long_words(10, "Hello World Foo"), ["Hello", "World", "Foo"])

    def test_edge_case_multiple_words_n_shorter_than_word(self):
        self.assertEqual(long_words(10, "Hello World Foo"), ["Hello", "World", "Foo"])

    def test_edge_case_multiple_words_n_equal_to_word(self):
        self.assertEqual(long_words(5, "Hello World Foo"), ["World", "Foo"])

    def test_edge_case_multiple_words_n_longer_than_word(self):
        self.assertEqual(long_words(10, "Hello World Foo"), ["World", "Foo"])

    def test_edge_case_multiple_words_n_shorter_than_word(self):
        self.assertEqual(long_words(10, "Hello World Foo"), ["World", "Foo"])

    def test_edge_case_multiple_words_n_equal_to_word(self):
        self.assertEqual(long_words(5, "Hello World Foo"), ["World", "Foo"])
