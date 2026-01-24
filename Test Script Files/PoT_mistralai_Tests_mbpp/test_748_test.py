import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")
        self.assertEqual(capital_words_spaces("PythonProgramming"), "Python Programming")

    def test_edge_case_single_word(self):
        self.assertEqual(capital_words_spaces("Hello"), "Hello " )
        self.assertEqual(capital_words_spaces("World"), " World")

    def test_edge_case_single_capital(self):
        self.assertEqual(capital_words_spaces("HeLlo"), "He Ll o")
        self.assertEqual(capital_words_spaces("PyTHoN"), "Py T H o N")

    def test_edge_case_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_edge_case_only_spaces(self):
        self.assertEqual(capital_words_spaces("   "), "  ")

    def test_edge_case_only_numbers(self):
        self.assertEqual(capital_words_spaces("12345"), "12345")
