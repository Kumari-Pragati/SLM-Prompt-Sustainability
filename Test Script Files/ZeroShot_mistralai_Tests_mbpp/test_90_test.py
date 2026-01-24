import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_element_list(self):
        self.assertEqual(len_log(['a']), 1)

    def test_list_with_single_long_element(self):
        self.assertEqual(len_log(['a', 'abcd']), 4)

    def test_list_with_multiple_long_elements(self):
        self.assertEqual(len_log(['abcd', '12345', 'xyz']), 5)

    def test_list_with_short_and_long_elements(self):
        self.assertEqual(len_log(['a', 'abcd', '1', '12345']), 5)
