import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_uppercase_only(self):
        self.assertEqual(remove_lowercase("HELLO"), "HELLO")

    def test_mixed_case(self):
        self.assertEqual(remove_lowercase("HelloWorld"), "HelloWorld")

    def test_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_only_lowercase(self):
        self.assertEqual(remove_lowercase("hello"), "")

    def test_special_characters(self):
        self.assertEqual(remove_lowercase("!@#$%^&*()_+-=[]{};':\"|,.<>/?HELLO"), "HELLO")
