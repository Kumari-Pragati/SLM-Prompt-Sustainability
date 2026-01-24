import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):
    def test_typical_use_case(self):
        texts = ['listen', 'silent', 'hello', 'world']
        str = 'enlist'
        self.assertEqual(anagram_lambda(texts, str), ['listen', 'silent'])

    def test_edge_case_single_character(self):
        texts = ['a', 'b', 'c']
        str = 'a'
        self.assertEqual(anagram_lambda(texts, str), ['a'])

    def test_boundary_case_empty_texts(self):
        texts = []
        str = 'hello'
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_boundary_case_empty_str(self):
        texts = ['hello', 'world']
        str = ''
        self.assertEqual(anagram_lambda(texts, str), [])

    def test_error_handling_invalid_input_type(self):
        texts = ['hello', 'world']
        str = 123  # Invalid input type
        with self.assertRaises(TypeError):
            anagram_lambda(texts, str)
