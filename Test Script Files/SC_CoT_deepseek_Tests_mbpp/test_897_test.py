import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Word_Present("This is a test sentence", "test"))

    def test_edge_case_word_at_start(self):
        self.assertTrue(is_Word_Present("test sentence", "test"))

    def test_edge_case_word_at_end(self):
        self.assertTrue(is_Word_Present("This is a test", "test"))

    def test_edge_case_word_only(self):
        self.assertTrue(is_Word_Present("test", "test"))

    def test_edge_case_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "test"))

    def test_edge_case_empty_word(self):
        self.assertFalse(is_Word_Present("This is a test sentence", ""))

    def test_corner_case_case_insensitive(self):
        self.assertTrue(is_Word_Present("This is a Test sentence", "test"))

    def test_corner_case_multiple_occurrences(self):
        self.assertTrue(is_Word_Present("This is a test sentence. Test again.", "test"))

    def test_corner_case_no_occurrences(self):
        self.assertFalse(is_Word_Present("This is a sentence", "test"))

    def test_invalid_input_none_sentence(self):
        with self.assertRaises(TypeError):
            is_Word_Present(None, "test")

    def test_invalid_input_none_word(self):
        with self.assertRaises(TypeError):
            is_Word_Present("This is a test sentence", None)

    def test_invalid_input_empty_sentence(self):
        with self.assertRaises(TypeError):
            is_Word_Present("", "test")
