import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(reverse_string_list([]), [])

    def test_single_element_list(self):
        self.assertListEqual(reverse_string_list(["hello"]), ["olleh"])

    def test_multiple_elements_list(self):
        self.assertListEqual(reverse_string_list(["hello", "world"]), ["olleh", "dlrow"])

    def test_mixed_case_list(self):
        self.assertListEqual(reverse_string_list(["Hello", "World"]), ["olleH", "dlrow"])

    def test_list_with_numbers(self):
        self.assertListEqual(reverse_string_list(["Hello", "123", "World"]), ["olleH", "321", "dlrow"])

    def test_list_with_special_characters(self):
        self.assertListEqual(reverse_string_list(["Hello@123", "World_"]), ["olleH@312", "drow_l"])

    def test_list_with_empty_string(self):
        self.assertListEqual(reverse_string_list(["Hello", "", "World"]), ["olleh", "", "dlrow"])

    def test_list_with_none(self):
        self.assertListEqual(reverse_string_list(["Hello", None, "World"]), ["olleh", None, "dlrow"])

    def test_list_with_non_string_element(self):
        with self.assertRaises(TypeError):
            reverse_string_list(["Hello", 123, "World"])
