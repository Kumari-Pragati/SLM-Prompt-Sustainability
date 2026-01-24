import unittest
from mbpp_254_code import words_ae

class TestWordsAe(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(words_ae("Hello, this is an example"), ["Hello", "an", "example"])

    def test_edge_case_empty_string(self):
        self.assertEqual(words_ae(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(words_ae("Hello"), [])

    def test_edge_case_no_a_or_e(self):
        self.assertEqual(words_ae("This is a test"), [])

    def test_edge_case_multiple_a_and_e(self):
        self.assertEqual(words_ae("AaEe test"), ["Aa", "Ee"])

    def test_edge_case_a_and_e_in_middle(self):
        self.assertEqual(words_ae("This is an example test"), ["an"])

    def test_edge_case_a_and_e_at_start(self):
        self.assertEqual(words_ae("AaEe test example"), ["Aa", "Ee"])

    def test_edge_case_a_and_e_at_end(self):
        self.assertEqual(words_ae("test example AaEe"), [])
