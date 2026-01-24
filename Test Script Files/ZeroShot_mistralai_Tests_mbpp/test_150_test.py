import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):

    def test_same_string(self):
        self.assertTrue(does_Contain_B("abc", "abc", 1))

    def test_different_strings_with_same_characters(self):
        self.assertTrue(does_Contain_B("abc", "cba", 1))

    def test_different_strings_with_different_characters(self):
        self.assertFalse(does_Contain_B("abc", "xyz", 1))

    def test_different_strings_with_same_characters_and_different_order(self):
        self.assertTrue(does_Contain_B("abc", "cab", 1))

    def test_different_strings_with_same_characters_and_different_order_and_different_length(self):
        self.assertTrue(does_Contain_B("abc", "abcd", 1))

    def test_different_strings_with_different_characters_and_same_length(self):
        self.assertFalse(does_Contain_B("abc", "123", 1))

    def test_different_strings_with_different_characters_and_different_length(self):
        self.assertFalse(does_Contain_B("abc", "123", 3))

    def test_different_strings_with_same_characters_and_different_length_and_different_order(self):
        self.assertTrue(does_Contain_B("abc", "abcd", 2))

    def test_different_strings_with_same_characters_and_different_length_and_different_order_and_different_gcd(self):
        self.assertFalse(does_Contain_B("abc", "abcd", 5))
