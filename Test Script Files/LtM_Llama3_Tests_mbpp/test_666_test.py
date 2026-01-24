import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_char("hello", "l"), 2)
        self.assertEqual(count_char("hello", "h"), 1)
        self.assertEqual(count_char("hello", "o"), 2)
        self.assertEqual(count_char("hello", "x"), 0)

    def test_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_single_char(self):
        self.assertEqual(count_char("a", "a"), 1)
        self.assertEqual(count_char("a", "b"), 0)

    def test_multiple_chars(self):
        self.assertEqual(count_char("hello world", "l"), 3)
        self.assertEqual(count_char("hello world", "o"), 3)
        self.assertEqual(count_char("hello world", "x"), 0)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_char(123, "a")

    def test_non_char_input(self):
        with self.assertRaises(TypeError):
            count_char("hello", 123)
