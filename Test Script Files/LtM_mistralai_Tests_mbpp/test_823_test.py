import unittest
from mbpp_823_code import check_substring

class TestCheckSubscription(unittest.TestCase):
    def test_simple_substring(self):
        self.assertEqual(check_substring("hello world", "hello"), "string starts with the given substring")
        self.assertEqual(check_substring("world hello", "hello"), "string starts with the given substring")

    def test_empty_inputs(self):
        self.assertEqual(check_substring("", "hello"), "entered string isnt a substring")
        self.assertEqual(check_substring("hello", ""), "entered string isnt a substring")
        self.assertEqual(check_substring("", ""), "entered string isnt a substring")

    def test_edge_cases(self):
        self.assertEqual(check_substring("hello", "he"), "string starts with the given substring")
        self.assertEqual(check_substring("hello", "helo"), "string doesnt start with the given substring")
        self.assertEqual(check_substring("hello", "hell"), "string doesnt start with the given substring")
        self.assertEqual(check_substring("hello", "hellow"), "string doesnt start with the given substring")

    def test_special_flags(self):
        self.assertEqual(check_substring("Hello World", "hello", flags=re.IGNORECASE), "string starts with the given substring")
        self.assertEqual(check_substring("Hello World", "HELLO", flags=re.IGNORECASE), "string starts with the given substring")
