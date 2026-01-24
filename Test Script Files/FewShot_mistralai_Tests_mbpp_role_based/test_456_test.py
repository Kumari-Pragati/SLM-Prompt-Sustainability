import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(reverse_string_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(reverse_string_list(["hello"]), ["olleh"])

    def test_multi_element_list(self):
        self.assertEqual(reverse_string_list(["hello", "world"]), ["dlrow", "olloh"])

    def test_list_with_numbers(self):
        self.assertEqual(reverse_string_list(["hello", "123"]), ["321", "olloh"])

    def test_list_with_special_characters(self):
        self.assertEqual(reverse_string_list(["hello@world", "123$"]), ["!$231", "world@lloh"])
