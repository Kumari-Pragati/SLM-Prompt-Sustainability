import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_uppercase("Hello, World!"), "hello, world")

    def test_edge_case_upper_boundary(self):
        self.assertEqual(remove_uppercase("A" * 100), " " * 100)

    def test_edge_case_lower_boundary(self):
        self.assertEqual(remove_uppercase("a" * 100), "a" * 100)

    def test_mixed_case_input(self):
        self.assertEqual(remove_uppercase("HeLlO, wOrLd!"), "hello, world")

    def test_empty_string(self):
        self.assertEqual(remove_uppercase(""), "")

    def test_single_uppercase_letter(self):
        self.assertEqual(remove_uppercase("A"), "")

    def test_single_uppercase_word(self):
        self.assertEqual(remove_uppercase("Hello"), "hello")

    def test_multiple_uppercase_words(self):
        self.assertEqual(remove_uppercase("Hello World"), "hello world")

    def test_special_characters(self):
        self.assertEqual(remove_uppercase("!@#$%^&*()_+-=[]{};':\"|,.<>/?HELLO, WORLD!"), "!@#$%^&*()_+-=[]{};':\"|,.<>/?hello, world")
