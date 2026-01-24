import unittest
from mbpp_823_code import check_substring

class TestCheckSubscription(unittest.TestCase):

    def test_substring_present(self):
        self.assertEqual(check_substring("HelloWorld", "Hello"), "string starts with the given substring")
        self.assertEqual(check_substring("WorldHello", "Hello"), "string starts with the given substring")
        self.assertEqual(check_substring("HelloWorld", "World"), "string doesnt start with the given substring")

    def test_substring_not_present(self):
        self.assertEqual(check_substring("HelloWorld", "Worlds"), "entered string isnt a substring")

    def test_empty_string(self):
        self.assertEqual(check_substring("", "Hello"), "entered string isnt a substring")

    def test_single_char_string(self):
        self.assertEqual(check_substring("a", "a"), "string starts with the given substring")
        self.assertEqual(check_substring("a", "b"), "entered string isnt a substring")

    def test_substring_at_beginning_and_end(self):
        self.assertEqual(check_substring("HelloWorld", "Hello"), "string starts with the given substring")
        self.assertEqual(check_substring("WorldHello", "Hello"), "string starts with the given substring")
        self.assertEqual(check_substring("HelloWorld", "World"), "string doesnt start with the given substring")

    def test_substring_case_sensitivity(self):
        self.assertEqual(check_substring("HelloWorld", "hello"), "entered string isnt a substring")
        self.assertEqual(check_substring("HelloWorld", "HELLO"), "string starts with the given substring")
