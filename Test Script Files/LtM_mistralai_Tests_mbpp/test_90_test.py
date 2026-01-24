import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(len_log([['a'], ['b'], ['c']]), 2)

    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_item_list(self):
        self.assertEqual(len_log(['abc']), 3)

    def test_longest_item_wins(self):
        self.assertEqual(len_log([['a'], ['ab'], ['abc']]), 3)

    def test_mixed_list(self):
        self.assertEqual(len_log([1, 'a', [2, 3]]), 2)

    def test_negative_list(self):
        self.assertEqual(len_log([[-1], [-2], [-3]]), 1)

    def test_empty_strings(self):
        self.assertEqual(len_log(['', ' ', '\t']), 0)

    def test_long_strings(self):
        self.assertEqual(len_log(['a' * 100, 'b' * 200, 'c' * 300]), 300)
