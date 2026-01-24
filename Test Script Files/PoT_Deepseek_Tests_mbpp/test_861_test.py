import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_typical_case(self):
        texts = ['cat', 'tac', 'act']
        str = 'cat'
        self.assertEqual(anagram_lambda(texts, str), ['cat', 'tac', 'act'])

    def test_edge_case_empty_string(self):
        texts = ['cat', 'tac', 'act']
        str = ''
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_edge_case_empty_texts(self):
        texts = []
        str = 'cat'
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_corner_case_single_character(self):
        texts = ['a', 'b', 'c']
        str = 'a'
        self.assertEqual(anagram_lambda(texts, str), ['a'])

    def test_corner_case_duplicates(self):
        texts = ['aabb', 'bbaa', 'abab']
        str = 'aabb'
        self.assertEqual(anagram_lambda(texts, str), ['aabb', 'bbaa', 'abab'])

    def test_corner_case_non_anagrams(self):
        texts = ['abc', 'def', 'ghi']
        str = 'abc'
        self.assertEqual(anagram_lambda(texts, str), [])
