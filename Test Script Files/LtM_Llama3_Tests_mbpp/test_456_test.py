import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(reverse_string_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(reverse_string_list(["hello"]), ["olleh"])

    def test_multiple_elements_list(self):
        self.assertEqual(reverse_string_list(["hello", "world"]), ["olleh", "dlrow"])

    def test_empty_string(self):
        self.assertEqual(reverse_string_list([""]), [""])

    def test_single_empty_string(self):
        self.assertEqual(reverse_string_list([""]), [""])

    def test_multiple_empty_strings(self):
        self.assertEqual(reverse_string_list(["", ""]), ["", ""])

    def test_long_string(self):
        self.assertEqual(reverse_string_list(["abcdefghijklmnopqrstuvwxyz"]), ["zyxwvutsrqponmlkjihgfedcba"])

    def test_long_string_list(self):
        self.assertEqual(reverse_string_list(["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"]), ["zyxwvutsrqponmlkjihgfedcba", "zyxwvutsrqponmlkjihgfedcba"])
