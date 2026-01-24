import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):
    def test_typical_use_case(self):
        text = "This is a test sentence. This sentence is a test."
        n = 3
        expected_result = [('This', 2), ('is', 2), ('a', 2)]
        self.assertEqual(n_common_words(text, n), expected_result)

    def test_edge_case_n_zero(self):
        text = "This is a test sentence. This sentence is a test."
        n = 0
        expected_result = []
        self.assertEqual(n_common_words(text, n), expected_result)

    def test_edge_case_n_greater_than_word_count(self):
        text = "This is a test sentence. This sentence is a test."
        n = 10
        expected_result = [('This', 2), ('is', 2), ('a', 2), ('test', 2), ('sentence', 2)]
        self.assertEqual(n_common_words(text, n), expected_result)

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
