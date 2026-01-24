import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(n_common_words("hello world hello again", 2), [("hello", 2), ("world", 1)])

    def test_edge_cases(self):
        self.assertEqual(n_common_words("", 2), [])
        self.assertEqual(n_common_words("a", 2), [("a", 1)])
        self.assertEqual(n_common_words("aaa", 2), [("aa", 2)])
        self.assertEqual(n_common_words("aaaabb", 2), [("aa", 2), ("bb", 1)])

    def test_boundary_cases(self):
        self.assertEqual(n_common_words("aabbcc", 3), [("a", 2), ("b", 2), ("c", 1)])
        self.assertEqual(n_common_words("aabbcc", 4), [("a", 2), ("b", 2), ("c", 1), ("", 1)])

    def test_special_cases(self):
        self.assertEqual(n_common_words("The quick brown fox jumps over the lazy dog", 3),
                         [("the", 2), ("brown", 1), ("fox", 1)])
        self.assertEqual(n_common_words("The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.", 3),
                         [("the", 4), ("quick", 3), ("brown", 2)])
