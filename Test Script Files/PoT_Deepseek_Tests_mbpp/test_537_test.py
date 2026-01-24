import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_repeated_word('Hello world world'), 'world')

    def test_edge_case_single_word(self):
        self.assertEqual(first_repeated_word('Hello'), 'None')

    def test_boundary_case_empty_string(self):
        self.assertEqual(first_repeated_word(''), 'None')

    def test_corner_case_repeated_word_at_end(self):
        self.assertEqual(first_repeated_word('Hello world world again'), 'world')

    def test_corner_case_repeated_word_at_start(self):
        self.assertEqual(first_repeated_word('world world again'), 'world')

    def test_corner_case_repeated_word_in_middle(self):
        self.assertEqual(first_repeated_word('Hello world world again'), 'world')

    def test_corner_case_repeated_word_with_different_cases(self):
        self.assertEqual(first_repeated_word('Hello World world'), 'World')

    def test_corner_case_repeated_word_with_punctuation(self):
        self.assertEqual(first_repeated_word('Hello, world world'), 'world')
