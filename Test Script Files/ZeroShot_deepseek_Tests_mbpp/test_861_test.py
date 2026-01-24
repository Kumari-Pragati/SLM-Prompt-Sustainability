import unittest
from mbpp_861_code import Counter
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_anagram_lambda(self):
        texts = ['cat', 'dog', 'act', 'god', 'tac', 'good', 'odg']
        str = 'cat'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, ['cat', 'act', 'tac'])

    def test_anagram_lambda_empty_texts(self):
        texts = []
        str = 'cat'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, [])

    def test_anagram_lambda_empty_str(self):
        texts = ['cat', 'dog', 'act', 'god', 'tac', 'good', 'odg']
        str = ''
        result = anagram_lambda(texts, str)
        self.assertEqual(result, [])

    def test_anagram_lambda_all_anagrams(self):
        texts = ['cat', 'dog', 'act', 'god', 'tac', 'good', 'odg']
        str = 'cat'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, ['cat', 'act', 'tac'])

    def test_anagram_lambda_no_anagrams(self):
        texts = ['cat', 'dog', 'act', 'god', 'tac', 'good', 'odg']
        str = 'abc'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, [])
