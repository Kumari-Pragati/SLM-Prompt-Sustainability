import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):
    def test_typical_input(self):
        text = "This is a test sentence. This sentence is a test."
        n = 3
        expected_output = [('This', 2), ('is', 2), ('a', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_n_zero(self):
        text = "This is a test sentence. This sentence is a test."
        n = 0
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_n_greater_than_length(self):
        text = "This is a test sentence. This sentence is a test."
        n = 10
        expected_output = [('This', 2), ('is', 2), ('a', 2), ('test', 2), ('sentence', 2), ('.', 2), ('', 1), ('This', 1), ('is', 1), ('a', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_invalid_input_non_integer_n(self):
        text = "This is a test sentence. This sentence is a test."
        n = 'three'
        with self.assertRaises(TypeError):
            n_common_words(text, n)

    def test_invalid_input_empty_text(self):
        text = ''
        n = 3
        with self.assertRaises(ZeroDivisionError):
            n_common_words(text, n)

    def test_invalid_input_non_string_text(self):
        text = 123
        n = 3
        with self.assertRaises(TypeError):
            n_common_words(text, n)
