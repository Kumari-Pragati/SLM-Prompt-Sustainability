import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(capital_words_spaces('HelloWorld'), 'Hello World')

    def test_single_capital_letter(self):
        self.assertEqual(capital_words_spaces('HelloW'), 'Hello W')

    def test_no_capital_letters(self):
        self.assertEqual(capital_words_spaces('helloworld'), 'helloworld')

    def test_empty_string(self):
        self.assertEqual(capital_words_spaces(''), '')

    def test_all_capital_letters(self):
        self.assertEqual(capital_words_spaces('HELLOWORLD'), 'HELLOWORLD')

    def test_mixed_case_with_spaces(self):
        self.assertEqual(capital_words_spaces('Hello WOrld'), 'Hello W Orld')

    def test_special_characters(self):
        self.assertEqual(capital_words_spaces('Hello$World'), 'Hello$World')

    def test_numbers_in_string(self):
        self.assertEqual(capital_words_spaces('Hello1World'), 'Hello1World')
