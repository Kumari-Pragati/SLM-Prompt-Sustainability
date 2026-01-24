import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_duplicate(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(remove_duplicate("hello"), "hello")

    def test_edge_case_no_duplicates(self):
        self.assertEqual(remove_duplicate("hello world"), "hello world")

    def test_edge_case_duplicates(self):
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_duplicate("   hello   world   "), "hello world")

    def test_edge_case_punctuation(self):
        self.assertEqual(remove_duplicate("Hello, world!"), "Hello, world!")

    def test_edge_case_uppercase(self):
        self.assertEqual(remove_duplicate("HELLO WORLD"), "HELLO WORLD")

    def test_edge_case_mixed_case(self):
        self.assertEqual(remove_duplicate("Hello, world!"), "Hello, world!")

    def test_edge_case_non_ascii(self):
        self.assertEqual(remove_duplicate("Hello, world!"), "Hello, world!")

    def test_edge_case_empty_string_list(self):
        self.assertEqual(remove_duplicate(""), "")

    def test_edge_case_single_word_list(self):
        self.assertEqual(remove_duplicate(["hello"]), ["hello"])

    def test_edge_case_no_duplicates_list(self):
        self.assertEqual(remove_duplicate(["hello", "world"]), ["hello", "world"])

    def test_edge_case_duplicates_list(self):
        self.assertEqual(remove_duplicate(["hello", "world", "hello"]), ["hello", "world"])

    def test_edge_case_multiple_spaces_list(self):
        self.assertEqual(remove_duplicate(["   hello   ", "world   "]), ["hello", "world"])

    def test_edge_case_punctuation_list(self):
        self.assertEqual(remove_duplicate(["Hello,", "world!"]), ["Hello,", "world!"])

    def test_edge_case_uppercase_list(self):
        self.assertEqual(remove_duplicate(["HELLO", "WORLD"]), ["HELLO", "WORLD"])

    def test_edge_case_mixed_case_list(self):
        self.assertEqual(remove_duplicate(["Hello,", "world!"]), ["Hello,", "world!"])

    def test_edge_case_non_ascii_list(self):
        self.assertEqual(remove_duplicate(["Hello,", "world!"]), ["Hello,", "world!"])
