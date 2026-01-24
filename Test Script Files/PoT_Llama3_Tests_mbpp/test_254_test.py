import unittest
from mbpp_254_code import words_ae

class TestWordsAe(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(words_ae("The aeolian harp is a beautiful instrument"), ['aeolian', 'ae'])

    def test_edge_case_empty_string(self):
        self.assertEqual(words_ae(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(words_ae("ae"), ['ae'])

    def test_edge_case_multiple_words(self):
        self.assertEqual(words_ae("ae ae ae"), ['ae', 'ae', 'ae'])

    def test_edge_case_non_alpha_input(self):
        self.assertEqual(words_ae("123 ae 456"), ['ae'])

    def test_edge_case_non_alpha_input2(self):
        self.assertEqual(words_ae("ae 123 456"), ['ae'])

    def test_edge_case_non_alpha_input3(self):
        self.assertEqual(words_ae("123 456 ae"), ['ae'])

    def test_edge_case_non_alpha_input4(self):
        self.assertEqual(words_ae("123 456 789"), [])

    def test_edge_case_non_alpha_input5(self):
        self.assertEqual(words_ae("ae 123 456 789"), ['ae'])

    def test_edge_case_non_alpha_input6(self):
        self.assertEqual(words_ae("123 ae 456 789"), ['ae'])

    def test_edge_case_non_alpha_input7(self):
        self.assertEqual(words_ae("123 456 ae 789"), ['ae'])

    def test_edge_case_non_alpha_input8(self):
        self.assertEqual(words_ae("123 456 789 ae"), [])

    def test_edge_case_non_alpha_input9(self):
        self.assertEqual(words_ae("123 456 789 ae 123"), ['ae'])

    def test_edge_case_non_alpha_input10(self):
        self.assertEqual(words_ae("123 456 789 ae 123 456"), ['ae'])
