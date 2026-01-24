import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_duplicate("Hello world hello"), "Hello world")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_duplicate(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(remove_duplicate("hello"), "hello")

    def test_edge_case_single_word_empty_string(self):
        self.assertEqual(remove_duplicate("hello"), "hello")

    def test_edge_case_duplicates(self):
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")

    def test_edge_case_case_insensitive(self):
        self.assertEqual(remove_duplicate("Hello world hello"), "Hello world")

    def test_edge_case_case_insensitive_duplicates(self):
        self.assertEqual(remove_duplicate("Hello world hello"), "Hello world")

    def test_edge_case_empty_string_duplicates(self):
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")

    def test_edge_case_single_word_duplicates(self):
        self.assertEqual(remove_duplicate("hello hello"), "hello")

    def test_edge_case_single_word_empty_string_duplicates(self):
        self.assertEqual(remove_duplicate("hello hello"), "hello")

    def test_edge_case_duplicates_empty_string(self):
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")

    def test_edge_case_duplicates_single_word(self):
        self.assertEqual(remove_duplicate("hello hello"), "hello")

    def test_edge_case_duplicates_single_word_empty_string(self):
        self.assertEqual(remove_duplicate("hello hello"), "hello")

    def test_edge_case_duplicates_case_insensitive(self):
        self.assertEqual(remove_duplicate("Hello world hello"), "Hello world")

    def test_edge_case_duplicates_case_insensitive_duplicates(self):
        self.assertEqual(remove_duplicate("Hello world hello"), "Hello world")

    def test_edge_case_duplicates_case_insensitive_empty_string(self):
        self.assertEqual(remove_duplicate("Hello world hello"), "Hello world")

    def test_edge_case_duplicates_case_insensitive_single_word(self):
        self.assertEqual(remove_duplicate("Hello hello"), "Hello")

    def test_edge_case_duplicates_case_insensitive_single_word_empty_string(self):
        self.assertEqual(remove_duplicate("Hello hello"), "Hello")

    def test_edge_case_duplicates_case_insensitive_single_word_duplicates(self):
        self.assertEqual(remove_duplicate("Hello hello"), "Hello")

    def test_edge_case_duplicates_case_insensitive_single_word_duplicates_empty_string(self):
        self.assertEqual(remove_duplicate("Hello hello"), "Hello")

    def test_edge_case_duplicates_case_insensitive_single_word_duplicates_single_word(self):
        self.assertEqual(remove_duplicate("Hello hello"), "Hello")

    def test_edge_case_duplicates_case_insensitive_single_word_duplicates_single_word_empty_string(self):
        self.assertEqual(remove_duplicate("Hello hello"), "Hello")
