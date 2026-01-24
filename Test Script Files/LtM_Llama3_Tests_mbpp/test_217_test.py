import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(first_Repeated_Char(""), '\0')

    def test_single_char_string(self):
        self.assertEqual(first_Repeated_Char("a"), 'a')

    def test_no_repeated_char(self):
        self.assertEqual(first_Repeated_Char("abc"), '\0')

    def test_repeated_char(self):
        self.assertEqual(first_Repeated_Char("aabb"), 'a')

    def test_repeated_char_at_start(self):
        self.assertEqual(first_Repeated_Char("aaab"), 'a')

    def test_repeated_char_at_end(self):
        self.assertEqual(first_Repeated_Char("abba"), 'b')

    def test_repeated_char_in_middle(self):
        self.assertEqual(first_Repeated_Char("abca"), 'a')

    def test_repeated_char_at_start_and_end(self):
        self.assertEqual(first_Repeated_Char("aabbcc"), 'a')

    def test_repeated_char_at_start_and_middle(self):
        self.assertEqual(first_Repeated_Char("aabbc"), 'a')

    def test_repeated_char_at_end_and_middle(self):
        self.assertEqual(first_Repeated_Char("abca"), 'a')
