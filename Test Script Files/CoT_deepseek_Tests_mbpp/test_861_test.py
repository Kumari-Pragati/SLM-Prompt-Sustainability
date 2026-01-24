import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_typical_case(self):
        texts = ['abc', 'bca', 'cab']
        str = 'abc'
        self.assertEqual(anagram_lambda(texts, str), ['abc', 'bca', 'cab'])

    def test_edge_case(self):
        texts = ['abc', 'bca', 'cab']
        str = ''
        self.assertEqual(anagram_lambda(texts, str), ['', '', ''])

    def test_boundary_case(self):
        texts = ['abc', 'bca', 'cab']
        str = 'a'
        self.assertEqual(anagram_lambda(texts, str), ['a', 'a', 'a'])

    def test_invalid_input(self):
        texts = ['abc', 'bca', 'cab']
        str = 123
        with self.assertRaises(TypeError):
            anagram_lambda(texts, str)
