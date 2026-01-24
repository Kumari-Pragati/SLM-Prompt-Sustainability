import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_word_present_in_sentence(self):
        self.assertTrue(is_Word_Present("This is a test sentence", "test"))

    def test_word_not_present_in_sentence(self):
        self.assertFalse(is_Word_Present("This is a test sentence", "absent"))

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "test"))

    def test_word_present_at_start_of_sentence(self):
        self.assertTrue(is_Word_Present("test sentence", "test"))

    def test_word_present_at_end_of_sentence(self):
        self.assertTrue(is_Word_Present("This is a test", "test"))

    def test_word_present_multiple_times(self):
        self.assertTrue(is_Word_Present("This is a test sentence. Test again.", "test"))

    def test_word_present_with_different_case(self):
        self.assertTrue(is_Word_Present("This is a Test sentence", "test"))

    def test_word_present_with_leading_trailing_spaces(self):
        self.assertTrue(is_Word_Present(" This is a test sentence ", "test"))

    def test_word_present_with_special_characters(self):
        self.assertTrue(is_Word_Present("This is a test! sentence", "test"))

    def test_word_present_with_numbers(self):
        self.assertTrue(is_Word_Present("This is a test123 sentence", "test123"))
