import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_item_list(self):
        self.assertEqual(len_log(['a']), 1)

    def test_list_of_single_char_strings(self):
        self.assertEqual(len_log(['a', 'b', 'c']), 1)

    def test_list_of_multi_char_strings(self):
        self.assertEqual(len_log(['abc', 'def', 'ghi']), 3)

    def test_list_of_strings_with_max_length(self):
        self.assertEqual(len_log(['a' * 10, 'b' * 10, 'c' * 10]), 10)

    def test_list_of_strings_with_min_length(self):
        self.assertEqual(len_log(['a', 'b', 'c'] * 10), 1)

    def test_list_of_strings_with_mixed_lengths(self):
        self.assertEqual(len_log(['a', 'ab', 'abc', 'abcd', 'abcde']), 5)
