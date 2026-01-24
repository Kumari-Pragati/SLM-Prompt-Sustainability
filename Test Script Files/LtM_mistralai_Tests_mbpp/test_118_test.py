import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(string_to_list("hello world"), ["hello", "world"])

    def test_empty_input(self):
        self.assertListEqual(string_to_list(""), [])

    def test_single_word_input(self):
        self.assertListEqual(string_to_list("example"), ["example"])

    def test_multiple_spaces_input(self):
        self.assertListEqual(string_to_list("one two three"), ["one", "two", "three"])

    def test_leading_trailing_spaces_input(self):
        self.assertListEqual(string_to_list("   one   two   three   "), ["one", "two", "three"])

    def test_non_alphanumeric_input(self):
        self.assertListEqual(string_to_list("123hello456world789"), ["123", "hello", "world", "789"])
