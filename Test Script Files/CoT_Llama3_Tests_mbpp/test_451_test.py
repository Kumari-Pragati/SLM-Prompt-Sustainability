import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):
    def test_remove_whitespaces(self):
        self.assertEqual(remove_whitespaces("Hello   World"), "HelloWorld")
        self.assertEqual(remove_whitespaces("   Hello   World   "), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello\nWorld"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello\tWorld"), "HelloWorld")
        self.assertEqual(remove_whitespaces("   \t\nHello   World   "), "HelloWorld")
        self.assertEqual(remove_whitespaces(""), "")
        self.assertEqual(remove_whitespaces("   "), "")
        self.assertEqual(remove_whitespaces("   \t\n"), "")

    def test_remove_multiple_spaces(self):
        self.assertEqual(remove_whitespaces("Hello   World   "), "HelloWorld")
        self.assertEqual(remove_whitespaces("   Hello   World   "), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello\nWorld\n"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello\tWorld\t"), "HelloWorld")
        self.assertEqual(remove_whitespaces("   \t\nHello   World   \n"), "HelloWorld")

    def test_remove_non_space_characters(self):
        self.assertEqual(remove_whitespaces("Hello World"), "Hello World")
        self.assertEqual(remove_whitespaces("Hello! World"), "Hello! World")
        self.assertEqual(remove_whitespaces("Hello, World"), "Hello, World")
        self.assertEqual(remove_whitespaces("Hello World?"), "Hello World?")
        self.assertEqual(remove_whitespaces("Hello World."), "Hello World.")
        self.assertEqual(remove_whitespaces("Hello World,"), "Hello World,")

    def test_remove_empty_string(self):
        self.assertEqual(remove_whitespaces(""), "")
