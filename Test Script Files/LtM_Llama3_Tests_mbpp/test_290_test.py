import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(max_length(['hello']), (5, 'hello'))

    def test_multiple_element_list(self):
        self.assertEqual(max_length(['hello', 'world']), (5, 'hello'))

    def test_list_with_empty_string(self):
        self.assertEqual(max_length(['hello', '', 'world']), (5, 'hello'))

    def test_list_with_longest_string(self):
        self.assertEqual(max_length(['hello', 'world', 'abcdefghijklmnopqrstuvwxyz']), (26, 'abcdefghijklmnopqrstuvwxyz'))

    def test_list_with_ties(self):
        self.assertEqual(max_length(['hello', 'world', 'abc']), (3, 'abc'))

    def test_list_with_empty_string_and_longest_string(self):
        self.assertEqual(max_length(['', 'abcdefghijklmnopqrstuvwxyz']), (26, 'abcdefghijklmnopqrstuvwxyz'))
