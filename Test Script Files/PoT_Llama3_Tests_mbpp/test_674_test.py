import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_duplicate(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(remove_duplicate("hello"), "hello")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_duplicate("   "), " ")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_duplicate("hello   world"), "hello world")

    def test_edge_case_duplicates(self):
        self.assertEqual(remove_duplicate("hello hello world"), "hello world")

    def test_edge_case_duplicates_and_spaces(self):
        self.assertEqual(remove_duplicate("hello hello   world"), "hello world")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_duplicate(123)
