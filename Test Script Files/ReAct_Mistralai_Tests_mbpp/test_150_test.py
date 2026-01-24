import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):

    def test_same_strings(self):
        self.assertTrue(does_Contain_B('abc', 'abc', 1))

    def test_different_strings_with_same_length(self):
        self.assertFalse(does_Contain_B('abc', 'def', 1))

    def test_different_strings_with_different_lengths(self):
        self.assertFalse(does_Contain_B('abc', 'defg', 1))

    def test_different_strings_with_same_length_and_difference_ignored(self):
        self.assertTrue(does_Contain_B('abc', 'ABC', 1))

    def test_different_strings_with_same_length_and_difference_ignored_reverse(self):
        self.assertTrue(does_Contain_B('ABC', 'abc', 1))

    def test_different_strings_with_same_length_and_difference_ignored_case_insensitive(self):
        self.assertTrue(does_Contain_B('abc', 'ABC', 1))
        self.assertTrue(does_Contain_B('ABC', 'abc', 1))

    def test_different_strings_with_same_length_and_difference_ignored_case_insensitive_reverse(self):
        self.assertTrue(does_Contain_B('ABC', 'abc', 1))
        self.assertTrue(does_Contain_B('abc', 'ABC', 1))

    def test_different_strings_with_same_length_and_difference_ignored_case_insensitive_reverse_with_step(self):
        self.assertTrue(does_Contain_B('ABC', 'abc', 2))
        self.assertTrue(does_Contain_B('abc', 'ABC', 2))

    def test_different_strings_with_same_length_and_difference_ignored_case_insensitive_reverse_with_step_negative(self):
        self.assertFalse(does_Contain_B('ABC', 'abc', -2))
        self.assertFalse(does_Contain_B('abc', 'ABC', -2))

    def test_same_string_with_step(self):
        self.assertTrue(does_Contain_B('abc', 'abc', 2))

    def test_same_string_with_step_negative(self):
        self.assertFalse(does_Contain_B('abc', 'abc', -2))

    def test_empty_strings(self):
        self.assertFalse(does_Contain_B('', '', 1))

    def test_empty_strings_with_step(self):
        self.assertFalse(does_Contain_B('', '', 2))

    def test_one_empty_string(self):
        self.assertFalse(does_Contain_B('abc', '', 1))

    def test_one_empty_string_with_step(self):
        self.assertFalse(does_Contain_B('abc', '', 2))

    def test_one_empty_string_with_step_negative(self):
        self.assertTrue(does_Contain_B('abc', '', -2))
