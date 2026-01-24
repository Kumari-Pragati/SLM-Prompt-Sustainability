import unittest
from mbpp_254_code import words_ae

class TestWordsAe(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(words_ae("The aeolian harp plays an aeolian tune"), ['aeolian', 'aeolian'])

    def test_edge_case_empty_string(self):
        self.assertEqual(words_ae(""), [])

    def test_edge_case_single_character(self):
        self.assertEqual(words_ae("a"), [])

    def test_edge_case_single_word(self):
        self.assertEqual(words_ae("hello"), [])

    def test_edge_case_multiple_words(self):
        self.assertEqual(words_ae("hello world"), [])

    def test_edge_case_multiple_ae(self):
        self.assertEqual(words_ae("ae ae ae"), ['ae', 'ae', 'ae'])

    def test_edge_case_multiple_ae_with_spaces(self):
        self.assertEqual(words_ae("ae ae ae"), ['ae', 'ae', 'ae'])

    def test_edge_case_multiple_ae_with_punctuation(self):
        self.assertEqual(words_ae("ae, ae. ae!"), ['ae', 'ae', 'ae'])

    def test_edge_case_multiple_ae_with_punctuation_and_spaces(self):
        self.assertEqual(words_ae("ae, ae. ae!"), ['ae', 'ae', 'ae'])

    def test_edge_case_multiple_e(self):
        self.assertEqual(words_ae("e e e"), ['e', 'e', 'e'])

    def test_edge_case_multiple_e_with_spaces(self):
        self.assertEqual(words_ae("e e e"), ['e', 'e', 'e'])

    def test_edge_case_multiple_e_with_punctuation(self):
        self.assertEqual(words_ae("e, e. e!"), ['e', 'e', 'e'])

    def test_edge_case_multiple_e_with_punctuation_and_spaces(self):
        self.assertEqual(words_ae("e, e. e!"), ['e', 'e', 'e'])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            words_ae(123)

    def test_invalid_input_non_string_list(self):
        with self.assertRaises(TypeError):
            words_ae([123, "hello"])

    def test_invalid_input_non_string_dict(self):
        with self.assertRaises(TypeError):
            words_ae({"hello": "world"})
