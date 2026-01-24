import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(reverse_string_list(["hello", "world"]), ["olleh", "dlrow"])

    def test_single_element_list(self):
        self.assertEqual(reverse_string_list(["abc"]), ["cba"])

    def test_empty_list(self):
        self.assertEqual(reverse_string_list([]), [])

    def test_list_with_numbers(self):
        self.assertEqual(reverse_string_list(["hello", "123"]), ["olleh", "321"])

    def test_list_with_special_characters(self):
        self.assertEqual(reverse_string_list(["hello@world", "!abc#$%"]), ["olleh@rdwl", "fcba#$%!"])
