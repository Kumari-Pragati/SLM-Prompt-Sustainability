import unittest
from mbpp_456_code import List

from 456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(reverse_string_list([]), [])

    def test_single_element_list(self):
        self.assertListEqual(reverse_string_list(["hello"]), ["olleh"])

    def test_multiple_elements_list(self):
        self.assertListEqual(reverse_string_list(["hello", "world"]), ["olloh", "dlrow"])

    def test_list_with_numbers_and_strings(self):
        self.assertListEqual(reverse_string_list(["hello", 123, "world"]), ["olloh", "321", "dlrow"])

    def test_list_with_special_characters(self):
        self.assertListEqual(reverse_string_list(["hello@example.com", "123_456"]), ["moc.levexamplenull@olleh", "654_321"])
