import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], reverse_string_list([]))

    def test_single_element_list(self):
        self.assertListEqual(["hello", "olleh"], reverse_string_list(["hello"]))

    def test_multiple_elements_list(self):
        self.assertListEqual(["hello", "world", "python"], reverse_string_list(["hello", "world", "python"]))

    def test_mixed_case_strings(self):
        self.assertListEqual(["PyThOn", "wOrLd", "hElLo"], reverse_string_list(["PyThOn", "wOrLd", "hElLo"]))

    def test_empty_string(self):
        self.assertListEqual([], reverse_string_list(["", " ", "\t"]))

    def test_whitespace_only_list(self):
        self.assertListEqual([" ", "\t", "\n"], reverse_string_list([" ", "\t", "\n"]))

    def test_invalid_input_type(self):
        self.assertRaises(TypeError, reverse_string_list, 123)
        self.assertRaises(TypeError, reverse_string_list, (1, 2, 3))
        self.assertRaises(TypeError, reverse_string_list, {"key": "value"})
