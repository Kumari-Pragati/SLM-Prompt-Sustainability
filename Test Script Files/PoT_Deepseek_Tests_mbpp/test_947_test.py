import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(len_log(['abc', 'defgh', 'ijklm']), 3)

    def test_single_element(self):
        self.assertEqual(len_log(['abc']), 3)

    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_longest_string(self):
        self.assertEqual(len_log(['abcdefgh', 'ijklm']), 8)

    def test_all_same_length(self):
        self.assertEqual(len_log(['abc', 'def', 'ghi']), 3)

    def test_empty_strings(self):
        self.assertEqual(len_log(['', 'abc', '']), 0)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            len_log(None)
