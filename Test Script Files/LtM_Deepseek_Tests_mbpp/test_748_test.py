import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")

    def test_edge_case_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_boundary_case_single_capital_letter(self):
        self.assertEqual(capital_words_spaces("H"), "H")

    def test_boundary_case_all_capital_letters(self):
        self.assertEqual(capital_words_spaces("HELLOWORLD"), "HELLOWORLD")

    def test_complex_case_multiple_capital_letters(self):
        self.assertEqual(capital_words_spaces("HelloWORLD"), "Hello WORLD")

    def test_complex_case_mixed_case_string(self):
        self.assertEqual(capital_words_spaces("helloWORLD"), "hello WORLD")
