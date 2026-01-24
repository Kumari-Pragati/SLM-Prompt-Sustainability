import unittest
from mbpp_604_code import Iterable
from 604_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("I am a test"), "test a am I")

    def test_edge_cases(self):
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words(" "), "")
        self.assertEqual(reverse_words("   "), "")
        self.assertEqual(reverse_words("word"), "word")
        self.assertEqual(reverse_words("word1 word2"), "word2 word1")
        self.assertEqual(reverse_words("word1 word2 word3"), "word3 word2 word1")

    def test_boundary_cases(self):
        self.assertEqual(reverse_words("word1word2"), "word2word1")
        self.assertEqual(reverse_words("word1word2word3"), "word3word2word1")
        self.assertEqual(reverse_words("word1word2word3word4"), "word4word3word2word1")

    def test_special_cases(self):
        self.assertEqual(reverse_words("A1 B2 C3"), "C3 B2 A1")
        self.assertEqual(reverse_words("A1 B2 C3 D4"), "D4 C3 B2 A1")
        self.assertEqual(reverse_words("A1 B2 C3 D4 E5"), "E5 D4 C3 B2 A1")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, reverse_words, 123)
        self.assertRaises(TypeError, reverse_words, (1, 2, 3))
        self.assertRaises(TypeError, reverse_words, [1, 2, 3])
        self.assertRaises(TypeError, reverse_words, {"a": 1, "b": 2})
