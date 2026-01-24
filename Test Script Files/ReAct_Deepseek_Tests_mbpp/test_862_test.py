import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_typical_case(self):
        text = "This is a test. This is only a test."
        n = 2
        expected_output = [('test', 2), ('this', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_single_most_common_word(self):
        text = "This is a test. This is only a test."
        n = 1
        expected_output = [('test', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_no_common_words(self):
        text = "No common words here."
        n = 2
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_empty_text(self):
        text = ""
        n = 2
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_large_n(self):
        text = "This is a test. This is only a test."
        n = 10
        expected_output = [('test', 2), ('this', 2), ('is', 2), ('a', 2), ('only', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_negative_n(self):
        text = "This is a test. This is only a test."
        n = -2
        with self.assertRaises(ValueError):
            n_common_words(text, n)

    def test_non_string_text(self):
        text = 12345
        n = 2
        with self.assertRaises(TypeError):
            n_common_words(text, n)

    def test_non_integer_n(self):
        text = "This is a test. This is only a test."
        n = "two"
        with self.assertRaises(TypeError):
            n_common_words(text, n)
