import unittest
from mbpp_604_code import str
from six.moves.range import range

from six04_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("Python unittest"), "unittest Python")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words(" "), "")
        self.assertEqual(reverse_words("word"), "word")
        self.assertEqual(reverse_words("word "), " word")
        self.assertEqual(reverse_words(" word "), " word ")
        self.assertEqual(reverse_words("word1 word2"), "2word1 word")
        self.assertEqual(reverse_words("word1 word2 word3"), "3word2 2word1 word")

    def test_complex_input(self):
        self.assertEqual(reverse_words("hello world, it's nice to meet you"),
                         "you meet you nice it's to world hello")
        self.assertEqual(reverse_words("Python unittest, this is a test"),
                         "test a is this test unittest Python")
        self.assertEqual(reverse_words("Python unittest, this is a test, with spaces"),
                         "spaces test a is this test with unittest Python")
