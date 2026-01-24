import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(len_log([]), None)

    def test_single_element_list(self):
        self.assertEqual(len_log(['hello']), 5)

    def test_multiple_element_list(self):
        self.assertEqual(len_log(['hello', 'world', 'abc']), 3)

    def test_list_with_empty_string(self):
        self.assertEqual(len_log(['hello', '', 'world']), 0)

    def test_list_with_empty_string_and_numbers(self):
        self.assertEqual(len_log(['hello', '', 'world', 123]), 0)

    def test_list_with_empty_string_and_numbers_and_chars(self):
        self.assertEqual(len_log(['hello', '', 'world', 123, 'abc']), 0)

    def test_list_with_empty_string_and_numbers_and_chars_and_empty_list(self):
        self.assertEqual(len_log(['hello', '', 'world', 123, 'abc', []]), 0)
