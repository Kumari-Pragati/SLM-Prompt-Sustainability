import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):
    def test_count_single_char_in_string(self):
        self.assertEqual(count_char("Hello", 'l'), 3)

    def test_count_char_not_in_string(self):
        self.assertEqual(count_char("Hello", 'z'), 0)

    def test_count_empty_string(self):
        self.assertEqual(count_char("", 'a'), 0)

    def test_count_char_at_boundary(self):
        self.assertEqual(count_char("A", 'A'), 1)

    def test_count_multiple_chars_in_string(self):
        self.assertEqual(count_char("Python", 't'), 2)

    def test_count_case_insensitive_char(self):
        self.assertEqual(count_char("Python", 'p'.lower()), 1)
