import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_typical_case(self):
        text = "hello world hello python python world"
        n = 2
        expected_output = [('world', 2), ('hello', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_n_zero(self):
        text = "hello world"
        n = 0
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_n_negative(self):
        text = "hello world"
        n = -1
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_boundary_case_n_greater_than_words(self):
        text = "hello world"
        n = 10
        expected_output = [('hello', 1), ('world', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_corner_case_empty_text(self):
        text = ""
        n = 2
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_corner_case_single_word(self):
        text = "python"
        n = 1
        expected_output = [('python', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)
