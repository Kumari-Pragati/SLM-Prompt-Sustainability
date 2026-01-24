import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_len_log(self):
        self.assertEqual(len_log(['abc', 'def', 'ghi']), 3)
        self.assertEqual(len_log(['abc', 'def', 'gh']), 2)
        self.assertEqual(len_log(['abc', 'def']), 3)
        self.assertEqual(len_log(['abc']), 3)
        self.assertEqual(len_log(['a']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', '