import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_list("HelloWorld"), ["Hello", "World"])

    def test_edge_case_empty_string(self):
        self.assertEqual(split_list(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(split_list("Hello"), ["Hello"])

    def test_edge_case_multiple_words(self):
        self.assertEqual(split_list("HelloWorld FooBar"), ["Hello", "World", "Foo", "Bar"])

    def test_edge_case_non_alphabetic_characters(self):
        self.assertEqual(split_list("Hello!World"), ["Hello", "World"])

    def test_edge_case_punctuation_at_end(self):
        self.assertEqual(split_list("Hello,World!"), ["Hello", "World"])

    def test_edge_case_punctuation_in_middle(self):
        self.assertEqual(split_list("Hello,World! Foo,Bar"), ["Hello", "World", "Foo", "Bar"])

    def test_edge_case_punctuation_at_start(self):
        self.assertEqual(split_list(",Hello,World!"), ["Hello", "World"])

    def test_edge_case_punctuation_at_start_and_end(self):
        self.assertEqual(split_list(",Hello,World!,Foo,Bar"), ["Hello", "World", "Foo", "Bar"])

    def test_edge_case_multiple_punctuation(self):
        self.assertEqual(split_list("Hello,,World!,Foo,Bar"), ["Hello", "World", "Foo", "Bar"])

    def test_edge_case_non_alphabetic_characters_at_start(self):
        self.assertEqual(split_list("!Hello,World!,Foo,Bar"), ["Hello", "World", "Foo", "Bar"])

    def test_edge_case_non_alphabetic_characters_at_end(self):
        self.assertEqual(split_list("Hello,World!,Foo,Bar!"), ["Hello", "World", "Foo", "Bar"])
