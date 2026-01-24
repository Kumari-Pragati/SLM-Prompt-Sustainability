import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):
    def test_uppercase_to_lowercase(self):
        self.assertEqual(toggle_string("HELLO"), "hello")

    def test_lowercase_to_uppercase(self):
        self.assertEqual(toggle_string("hello"), "HELLO")

    def test_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(toggle_string("a"), "A")

    def test_mixed_case_string(self):
        self.assertEqual(toggle_string("HeLlO wOrLd"), "hello world")
