import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_typical_case(self):
        texts = ['cat', 'tac', 'dog', 'god']
        str = 'cat'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, ['cat', 'tac'])

    def test_edge_case(self):
        texts = ['a', 'b', 'c']
        str = 'a'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, ['a'])

    def test_corner_case(self):
        texts = ['abc', 'bca', 'cab']
        str = 'abc'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, ['abc', 'bca', 'cab'])

    def test_invalid_input(self):
        texts = ['cat', 'tac', 'dog', 'god']
        str = 123  # Invalid input
        with self.assertRaises(TypeError):
            anagram_lambda(texts, str)
