import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_simple_anagrams(self):
        texts = ['abc', 'bca', 'cab']
        self.assertEqual(anagram_lambda(texts, 'abc'), texts)

    def test_edge_case_empty_texts(self):
        self.assertEqual(anagram_lambda([], 'abc'), [])

    def test_edge_case_empty_str(self):
        texts = ['abc', 'bca', 'cab']
        self.assertEqual(anagram_lambda(texts, ''), [])

    def test_boundary_case_single_character(self):
        texts = ['a', 'b', 'c']
        self.assertEqual(anagram_lambda(texts, 'a'), ['a'])

    def test_complex_case_anagrams_with_duplicates(self):
        texts = ['aabb', 'abab', 'bbaa']
        self.assertEqual(anagram_lambda(texts, 'aabb'), texts)

    def test_complex_case_non_anagrams(self):
        texts = ['abc', 'def', 'ghi']
        self.assertEqual(anagram_lambda(texts, 'abc'), ['abc'])
