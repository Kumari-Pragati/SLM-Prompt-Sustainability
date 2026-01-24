import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_max_length(self):
        self.assertEqual(len_log(['abc', 'defgh', 'ijkl']), 5)

    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_element(self):
        self.assertEqual(len_log(['abcdefgh']), 8)

    def test_all_same_length(self):
        self.assertEqual(len_log(['abc', 'def', 'ghi']), 3)

    def test_long_strings(self):
        self.assertEqual(len_log(['abcdefghijklmnopqrstuvwxyz', '1234567890']), 10)
