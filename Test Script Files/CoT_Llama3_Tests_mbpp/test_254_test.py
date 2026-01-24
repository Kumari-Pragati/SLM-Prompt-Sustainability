import unittest
from mbpp_254_code import words_ae

class TestWordsAe(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(words_ae("The aeagle soars aebove"), ["aeagle", "aebove"])

    def test_edge_case_empty_string(self):
        self.assertEqual(words_ae(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(words_ae("aeagle"), ["aeagle"])

    def test_edge_case_single_character(self):
        self.assertEqual(words_ae("a"), [])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(words_ae("   aeagle   "), ["aeagle"])

    def test_edge_case_punctuation(self):
        self.assertEqual(words_ae("The aeagle soars aebove!"), ["aeagle", "aebove"])

    def test_edge_case_numbers(self):
        self.assertEqual(words_ae("The aeagle soars aebove 123"), ["aeagle", "aebove"])

    def test_edge_case_uppercase(self):
        self.assertEqual(words_ae("The AEAGLE soars AEabove"), [])

    def test_edge_case_non_ascii(self):
        self.assertEqual(words_ae("The æagle soars æbove"), ["æagle", "æbove"])

    def test_edge_case_multiple_ae(self):
        self.assertEqual(words_ae("The ae aeagle soars ae aeabove"), ["aeagle", "aeabove"])

    def test_edge_case_ae_at_start(self):
        self.assertEqual(words_ae("aeagle soars aeabove"), ["aeagle", "aeabove"])

    def test_edge_case_ae_at_end(self):
        self.assertEqual(words_ae("The aeagle soars aeabove ae"), ["aeagle", "aeabove"])
