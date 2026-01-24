import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(len_log([]), None)

    def test_single_element_list(self):
        self.assertEqual(len_log(['hello']), 5)

    def test_multiple_elements_list(self):
        self.assertEqual(len_log(['hello', 'world']), 5)

    def test_list_with_empty_string(self):
        self.assertEqual(len_log(['hello', '', 'world']), 5)

    def test_list_with_longest_string(self):
        self.assertEqual(len_log(['hello', 'world', 'thisisaverylongstring']), 24)

    def test_list_with_tied_longest_strings(self):
        self.assertEqual(len_log(['hello', 'world', 'thisisaverylongstring', 'thisisaverylongstring']), 24)

    def test_list_with_negative_length(self):
        with self.assertRaises(TypeError):
            len_log(['hello', 'world', 'thisisaverylongstring', -1])
