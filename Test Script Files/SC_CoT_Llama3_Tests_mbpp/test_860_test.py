import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_acceptable_string(self):
        self.assertEqual(check_alphanumeric("hello123"), "Accept")

    def test_unacceptable_string(self):
        self.assertEqual(check_alphanumeric("hello world"), "Discard")

    def test_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_single_character(self):
        self.assertEqual(check_alphanumeric("a"), "Accept")

    def test_non_alphanumeric_character(self):
        self.assertEqual(check_alphanumeric("hello!"), "Discard")

    def test_multiple_non_alphanumeric_characters(self):
        self.assertEqual(check_alphanumeric("hello!@#"), "Discard")

    def test_single_non_alphanumeric_character(self):
        self.assertEqual(check_alphanumeric("hello!"), "Discard")

    def test_multiple_alphanumeric_characters(self):
        self.assertEqual(check_alphanumeric("hello123456"), "Accept")

    def test_single_alphanumeric_character(self):
        self.assertEqual(check_alphanumeric("a"), "Accept")

    def test_mixed_alphanumeric_characters(self):
        self.assertEqual(check_alphanumeric("hello123abc"), "Accept")

    def test_string_with_spaces(self):
        self.assertEqual(check_alphanumeric("hello world"), "Discard")

    def test_string_with_punctuation(self):
        self.assertEqual(check_alphanumeric("hello!"), "Discard")

    def test_string_with_digits(self):
        self.assertEqual(check_alphanumeric("hello123"), "Accept")

    def test_string_with_uppercase(self):
        self.assertEqual(check_alphanumeric("HELLO"), "Accept")

    def test_string_with_lowercase(self):
        self.assertEqual(check_alphanumeric("hello"), "Accept")

    def test_string_with_mixed_case(self):
        self.assertEqual(check_alphanumeric("Hello123"), "Accept")

    def test_string_with_non_alphanumeric_characters_at_end(self):
        self.assertEqual(check_alphanumeric("hello123!"), "Discard")

    def test_string_with_non_alphanumeric_characters_in_middle(self):
        self.assertEqual(check_alphanumeric("hello!123"), "Discard")

    def test_string_with_non_alphanumeric_characters_at_start(self):
        self.assertEqual(check_alphanumeric("!hello123"), "Discard")

    def test_string_with_non_alphanumeric_characters_at_start_and_end(self):
        self.assertEqual(check_alphanumeric("!hello!123"), "Discard")
