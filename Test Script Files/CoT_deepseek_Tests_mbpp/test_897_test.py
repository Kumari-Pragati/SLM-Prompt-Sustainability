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

    def test_edge_case_word_not_present(self):
        self.assertFalse(is_Word_Present("This is a test sentence", "absent"))

    def test_edge_case_case_sensitivity(self):
        self.assertFalse(is_Word_Present("This is a Test sentence", "test"))

    def test_edge_case_multiple_spaces(self):
        self.assertTrue(is_Word_Present("This  is a   test sentence", "test"))

    def test_edge_case_punctuation(self):
        self.assertTrue(is_Word_Present("This is a test sentence!", "test"))
        self.assertTrue(is_Word_Present("This is a test sentence,", "test"))
        self.assertTrue(is_Word_Present("This is a test sentence?", "test"))
