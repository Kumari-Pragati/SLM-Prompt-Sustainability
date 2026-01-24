import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_same_strings(self):
        self.assertTrue(does_Contain_B('abc', 'abc', 1))

    def test_different_strings_with_same_length(self):
        self.assertFalse(does_Contain_B('abc', 'def', 1))

    def test_different_strings_with_different_lengths_and_same_characters(self):
        self.assertTrue(does_Contain_B('aa', 'bb', 1))

    def test_different_strings_with_different_lengths_and_different_characters(self):
        self.assertFalse(does_Contain_B('abc', 'def', 1))

    def test_different_strings_with_same_length_and_different_characters_but_same_difference(self):
        self.assertTrue(does_Contain_B('aaa', 'bbb', 3))

    def test_different_strings_with_same_length_and_different_characters_but_different_difference(self):
        self.assertFalse(does_Contain_B('aaa', 'bbb', 2))

    def test_invalid_input_non_string(self):
        self.assertRaises(TypeError, does_Contain_B, 1, 2, 3)

    def test_invalid_input_negative_coefficient(self):
        self.assertRaises(ValueError, does_Contain_B, 'abc', 'def', -1)
