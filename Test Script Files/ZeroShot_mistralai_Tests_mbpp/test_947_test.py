import unittest
from947_code import len_log

class TestLenLog(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_element_list(self):
        self.assertEqual(len_log(['a']), 1)

    def test_multiple_elements_with_same_length(self):
        self.assertEqual(len_log(['aa', 'bb', 'cc']), 2)

    def test_multiple_elements_with_different_lengths(self):
        self.assertEqual(len_log(['aa', 'ab', 'abc']), 3)

    def test_negative_list(self):
        self.assertEqual(len_log([-1, -2, -3]), 1)

    def test_list_with_empty_strings(self):
        self.assertEqual(len_log(['', 'a', 'b']), 1)

    def test_list_with_none(self):
        self.assertEqual(len_log(['a', None, 'b']), 2)
