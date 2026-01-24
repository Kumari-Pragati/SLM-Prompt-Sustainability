import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(remove_words(['hello world', 'apple banana'], ['o']), ['hello', 'banana'])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_words([], ['a']), [])

    def test_edge_case_empty_charlist(self):
        self.assertEqual(remove_words(['hello', 'world'], []), ['hello', 'world'])

    def test_edge_case_single_word(self):
        self.assertEqual(remove_words(['apple'], ['a']), [])

    def test_edge_case_single_char_in_word(self):
        self.assertEqual(remove_words(['hello', 'apple'], ['l']), ['apple'])

    def test_edge_case_multiple_chars_in_word(self):
        self.assertEqual(remove_words(['hello', 'apple'], ['ll']), [])

    def test_edge_case_char_in_beginning_and_end(self):
        self.assertEqual(remove_words(['hello', 'apple'], ['h', 'e']), ['apple'])

    def test_edge_case_char_in_middle_of_word(self):
        self.assertEqual(remove_words(['hello', 'apple'], ['llo']), [])

    def test_complex_case_multiple_chars_in_different_words(self):
        self.assertEqual(remove_words(['hello world', 'apple banana'], ['o', 'a']), ['world', 'banana'])
