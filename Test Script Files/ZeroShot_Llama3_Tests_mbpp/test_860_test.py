import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("HelloWorld123"), "Accept")

    def test_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("Hello World!"), "Discard")

    def test_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_single_character_string(self):
        self.assertEqual(check_alphanumeric("a"), "Accept")

    def test_single_character_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric(" "), "Discard")

    def test_multiple_character_string(self):
        self.assertEqual(check_alphanumeric("HelloWorld"), "Accept")

    def test_multiple_character_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("Hello World"), "Discard")
