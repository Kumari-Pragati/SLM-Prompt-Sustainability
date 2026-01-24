import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_string_to_list(self):
        self.assertEqual(string_to_list("Hello World"), ["Hello", "World"])
        self.assertEqual(string_to_list(""), [])
        self.assertEqual(string_to_list("   "), [""])
        self.assertEqual(string_to_list("Hello"), ["Hello"])
        self.assertEqual(string_to_list("Hello World, this is a test"), ["Hello", "World,", "this", "is", "a", "test"])
        self.assertEqual(string_to_list("   Hello   World   "), ["", "Hello", "", "World", ""])

    def test_string_to_list_edge_cases(self):
        self.assertEqual(string_to_list(None), [])
        self.assertEqual(string_to_list("   "), [""])
        self.assertEqual(string_to_list(""), [])
