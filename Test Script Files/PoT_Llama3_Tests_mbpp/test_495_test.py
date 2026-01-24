import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_lowercase("Hello World"), "HW")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_edge_case_single_lowercase_character(self):
        self.assertEqual(remove_lowercase("a"), "")

    def test_edge_case_single_uppercase_character(self):
        self.assertEqual(remove_lowercase("A"), "A")

    def test_edge_case_multiple_lowercase_characters(self):
        self.assertEqual(remove_lowercase("abc"), "")

    def test_edge_case_multiple_uppercase_characters(self):
        self.assertEqual(remove_lowercase("ABC"), "ABC")

    def test_edge_case_mixed_case_characters(self):
        self.assertEqual(remove_lowercase("AbC"), "C")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)
