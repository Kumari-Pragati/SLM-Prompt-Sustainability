import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_string_list(["hello", "world"]), ["olleh", "dlrow"])

    def test_empty_list(self):
        self.assertEqual(reverse_string_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(reverse_string_list(["abc"]), ["cba"])

    def test_list_with_empty_string(self):
        self.assertEqual(reverse_string_list(["", "hello", "world"]), ["", "olleh", "dlrow"])

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            reverse_string_list([1, "hello", "world"])

    def test_list_with_mixed_case(self):
        self.assertEqual(reverse_string_list(["Hello", "WORLD"]), ["olleH", "dlroW"])
