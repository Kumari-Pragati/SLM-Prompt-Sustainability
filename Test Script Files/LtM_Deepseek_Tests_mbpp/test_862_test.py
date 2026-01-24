import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_simple_input(self):
        text = "hello world hello python"
        n = 2
        expected_output = [('hello', 2), ('world', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_empty_text(self):
        text = ""
        n = 1
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_empty_n(self):
        text = "hello world"
        n = 0
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_boundary_case_minimum_n(self):
        text = "hello world hello python"
        n = 1
        expected_output = [('hello', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_boundary_case_maximum_n(self):
        text = "hello world hello python"
        n = 5
        expected_output = [('hello', 2), ('world', 1), ('python', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_complex_case_multiple_words(self):
        text = "hello world hello python python"
        n = 3
        expected_output = [('hello', 2), ('python', 2), ('world', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_complex_case_same_frequency(self):
        text = "hello world hello python python"
        n = 4
        expected_output = [('hello', 2), ('python', 2), ('world', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)
