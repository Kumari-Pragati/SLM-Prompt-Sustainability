import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(capital_words_spaces('HelloWorld'), 'Hello World')

    def test_edge_case_single_capital(self):
        self.assertEqual(capital_words_spaces('H'), 'H')

    def test_boundary_case_all_capitals(self):
        self.assertEqual(capital_words_spaces('HELLOWORLD'), 'HELLOWORLD')

    def test_corner_case_no_capital(self):
        self.assertEqual(capital_words_spaces('helloworld'), 'helloworld')

    def test_corner_case_multiple_consecutive_capitals(self):
        self.assertEqual(capital_words_spaces('HelloWORLD'), 'Hello WORLD')

    def test_corner_case_multiple_spaces(self):
        self.assertEqual(capital_words_spaces('Hello   WORLD'), 'Hello   WORLD')

    def test_corner_case_empty_string(self):
        self.assertEqual(capital_words_spaces(''), '')
