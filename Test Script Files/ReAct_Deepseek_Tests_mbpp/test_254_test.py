import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):

    def test_typical_case(self):
        text = "apple banana orange"
        expected_output = ['apple', 'banana', 'orange']
        self.assertEqual(words_ae(text), expected_output)

    def test_edge_case_single_word(self):
        text = "apple"
        expected_output = ['apple']
        self.assertEqual(words_ae(text), expected_output)

    def test_edge_case_empty_string(self):
        text = ""
        expected_output = []
        self.assertEqual(words_ae(text), expected_output)

    def test_edge_case_no_ae_words(self):
        text = "xyz"
        expected_output = []
        self.assertEqual(words_ae(text), expected_output)

    def test_edge_case_special_characters(self):
        text = "a!b@c#d$e%f^g&h*i(j)k_l+m=n?o/p\\q\"r's{t}u[v]x|y:z;"
        expected_output = ['a!b@c#d$e%f^g&h*i(j)k_l+m=n?o/p\\q\"r\'s{t}u[v]x|y:z']
        self.assertEqual(words_ae(text), expected_output)

    def test_error_case_non_string_input(self):
        with self.assertRaises(TypeError):
            words_ae(123)
