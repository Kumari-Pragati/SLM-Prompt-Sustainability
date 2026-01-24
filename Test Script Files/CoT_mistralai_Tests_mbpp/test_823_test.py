import unittest
from mbpp_823_code import check_substring

class TestCheckSubscription(unittest.TestCase):
    def test_substring_present(self):
        self.assertEqual(check_substring("HelloWorld", "Hello"), "string starts with the given substring")
        self.assertEqual(check_substring("WorldHello", "Hello"), "string starts with the given substring")

    def test_substring_not_present(self):
        self.assertEqual(check_substring("HelloWorld", "World"), "entered string isnt a substring")
        self.assertEqual(check_substring("WorldHello", "HelloWorld"), "entered string isnt a substring")

    def test_empty_string(self):
        self.assertEqual(check_substring("", "Hello"), "entered string isnt a substring")

    def test_single_char_input(self):
        self.assertEqual(check_substring("a", "a"), "string starts with the given substring")
        self.assertEqual(check_substring("b", "a"), "entered string isnt a substring")

    def test_sample_starts_with_regex(self):
        self.assertEqual(check_substring("HelloWorld", "\AHello"), "string starts with the given substring")
        self.assertEqual(check_subscription("WorldHello", "\AHello"), "entered string isnt a substring")

    def test_sample_not_a_string(self):
        self.assertRaises(TypeError, check_substring, "Hello", 123)
        self.assertRaises(TypeError, check_substring, 123, "Hello")
