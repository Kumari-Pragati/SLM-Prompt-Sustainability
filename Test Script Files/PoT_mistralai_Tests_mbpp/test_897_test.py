import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Word_Present("hello world", "hello"))
        self.assertTrue(is_Word_Present("apple banana", "apple"))
        self.assertTrue(is_Word_Present("cat dog cat", "cat"))

    def test_edge_case_empty_string(self):
        self.assertFalse(is_Word_Present("", "word"))

    def test_edge_case_single_word(self):
        self.assertTrue(is_Word_Present("word", "word"))

    def test_edge_case_single_letter(self):
        self.assertTrue(is_Word_Present("a", "a"))
        self.assertFalse(is_Word_Present("a", "b"))

    def test_edge_case_whitespace_only(self):
        self.assertFalse(is_Word_Present("   ", "word"))

    def test_edge_case_punctuation(self):
        self.assertTrue(is_Word_Present("word,", "word"))
        self.assertFalse(is_Word_Present("word,", ","))

    def test_edge_case_case_sensitivity(self):
        self.assertFalse(is_Word_Present("Hello World", "hello"))
