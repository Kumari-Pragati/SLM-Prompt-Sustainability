import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_item_list(self):
        self.assertEqual(len_log(['a']), 1)

    def test_list_with_different_lengths(self):
        self.assertEqual(len_log(['a', 'b', 'c', 'd']), 3)

    def test_list_with_min_length(self):
        self.assertEqual(len_log(['a', 'aa', 'aaa']), 3)

    def test_list_with_min_length_at_end(self):
        self.assertEqual(len_log(['aa', 'aaa', 'a']), 3)

    def test_list_with_negative_lengths(self):
        self.assertRaises(ValueError, len_log, ['-1', '0', '1'])
