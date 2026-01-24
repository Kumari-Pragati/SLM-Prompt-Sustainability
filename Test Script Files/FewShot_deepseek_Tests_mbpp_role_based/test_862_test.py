import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):
    def test_typical_use_case(self):
        text = "hello world hello python python world"
        n = 2
        expected_output = [('world', 2), ('hello', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case_single_word(self):
        text = "python"
        n = 1
        expected_output = [('python', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_boundary_case_multiple_words(self):
        text = "hello world hello python python world"
        n = 3
        expected_output = [('world', 2), ('hello', 2), ('python', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_boundary_case_same_frequency(self):
        text = "hello world hello python python world"
        n = 4
        expected_output = [('world', 2), ('hello', 2), ('python', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_invalid_input_negative_n(self):
        text = "hello world hello python python world"
        n = -1
        with self.assertRaises(ValueError):
            n_common_words(text, n)

    def test_invalid_input_zero_n(self):
        text = "hello world hello python python world"
        n = 0
        with self.assertRaises(ValueError):
            n_common_words(text, n)
