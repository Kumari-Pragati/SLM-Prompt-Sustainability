import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(len_log([['a'], ['b'], ['c']]), 1)

    def test_single_input(self):
        self.assertEqual(len_log(['abc']), 3)

    def test_empty_input(self):
        self.assertEqual(len_log([]), 0)

    def test_single_empty_input(self):
        self.assertEqual(len_log(['']), 0)

    def test_long_input(self):
        self.assertEqual(len_log(['a' * 1000]), 1000)

    def test_short_input(self):
        self.assertEqual(len_log(['a'] * 10), 1)

    def test_mixed_input(self):
        self.assertEqual(len_log([['a'], ['ab'], ['abc']]), 2)
