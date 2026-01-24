import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_count_char_with_valid_input(self):
        self.assertEqual(count_char('hello', 'l'), 2)
        self.assertEqual(count_char('world', 'o'), 1)
        self.assertEqual(count_char('aaaaa', 'a'), 5)

    def test_count_char_with_empty_string(self):
        self.assertEqual(count_char('', 'a'), 0)

    def test_count_char_with_non_existing_char(self):
        self.assertEqual(count_char('hello', 'z'), 0)

    def test_count_char_with_case_sensitive_char(self):
        self.assertEqual(count_char('Hello', 'h'), 0)
