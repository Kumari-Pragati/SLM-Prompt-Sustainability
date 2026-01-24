import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello World")
        self.assertEqual(capitalize_first_last_letters("Hello, World!"), "Hello, World!")
        self.assertEqual(capitalize_first_last_letters("12345"), "12345")
        self.assertEqual(capitalize_first_last_letters("Hello_World"), "Hello_World")

    def test_edge_case_single_word(self):
        self.assertEqual(capitalize_first_last_letters(""), "")
        self.assertEqual(capitalize_first_last_letters("a"), "A")
        self.assertEqual(capitalize_first_last_letters("A"), "A")

    def test_edge_case_no_spaces(self):
        self.assertEqual(capitalize_first_last_letters("helloWorld"), "HelloWorld")
        self.assertEqual(capitalize_first_last_letters("HelloWorld"), "HelloWorld")

    def test_edge_case_empty_list(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_corner_case_empty_string_with_spaces(self):
        self.assertEqual(capitalize_first_last_letters(" "), "")

    def test_corner_case_single_uppercase_letter(self):
        self.assertEqual(capitalize_first_last_letters("A"), "A")

    def test_corner_case_single_lowercase_letter(self):
        self.assertEqual(capitalize_first_last_letters("a"), "A")
