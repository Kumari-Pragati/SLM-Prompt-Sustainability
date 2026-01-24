import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_string_length(self):
        self.assertEqual(string_length(""), 0)
        self.assertEqual(string_length("a"), 1)
        self.assertEqual(string_length("abc"), 3)
        self.assertEqual(string_length("hello"), 5)
        self.assertEqual(string_length("abcdef"), 6)
        self.assertEqual(string_length("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            string_length(123)
        with self.assertRaises(TypeError):
            string_length([1, 2, 3])
        with self.assertRaises(TypeError):
            string_length({"a": 1, "b": 2})
