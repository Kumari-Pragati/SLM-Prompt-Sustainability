import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_typical_case(self):
        texts = ['listen', 'silent', 'hello', 'world']
        str = 'enlist'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, ['listen', 'silent'])

    def test_empty_texts(self):
        texts = []
        str = 'hello'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, [])

    def test_empty_str(self):
        texts = ['listen', 'silent', 'hello', 'world']
        str = ''
        result = anagram_lambda(texts, str)
        self.assertEqual(result, [])

    def test_all_anagrams(self):
        texts = ['abc', 'bca', 'cab']
        str = 'abc'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, ['abc', 'bca', 'cab'])

    def test_no_anagrams(self):
        texts = ['abc', 'def', 'ghi']
        str = 'jkl'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, [])

    def test_case_sensitivity(self):
        texts = ['Listen', 'silent', 'hello', 'world']
        str = 'enlist'
        result = anagram_lambda(texts, str)
        self.assertEqual(result, [])
