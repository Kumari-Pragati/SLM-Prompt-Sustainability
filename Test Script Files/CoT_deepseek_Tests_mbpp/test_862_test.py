import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_typical_case(self):
        text = "hello world hello python python world"
        n = 2
        expected_output = [('world', 2), ('hello', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_single_most_common_word(self):
        text = "hello hello hello"
        n = 1
        expected_output = [('hello', 3)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_no_common_words(self):
        text = "one two three"
        n = 2
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_empty_text(self):
        text = ""
        n = 1
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_n_greater_than_number_of_unique_words(self):
        text = "hello world"
        n = 3
        expected_output = [('hello', 1), ('world', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_invalid_n_negative(self):
        text = "hello world"
        n = -1
        with self.assertRaises(ValueError):
            n_common_words(text, n)

    def test_invalid_n_zero(self):
        text = "hello world"
        n = 0
        with self.assertRaises(ValueError):
            n_common_words(text, n)
