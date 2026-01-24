import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_words(['apple', 'banana', 'cherry'], ['banana', 'cherry']), ['apple'])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_words([], ['apple']), [])

    def test_edge_case_empty_removewords(self):
        self.assertEqual(remove_words(['apple', 'banana', 'cherry'], []), ['apple', 'banana', 'cherry'])

    def test_corner_case_repeated_words(self):
        self.assertEqual(remove_words(['apple', 'apple', 'banana'], ['apple']), ['banana'])

    def test_corner_case_all_words_to_remove(self):
        self.assertEqual(remove_words(['apple', 'banana', 'cherry'], ['apple', 'banana', 'cherry']), [])
