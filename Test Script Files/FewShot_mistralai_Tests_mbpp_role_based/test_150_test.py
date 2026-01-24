import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_same_strings(self):
        self.assertTrue(does_Contain_B('abc', 'abc', 1))

    def test_different_strings(self):
        self.assertFalse(does_Contain_B('abc', 'def', 1))

    def test_different_strings_with_same_length(self):
        self.assertFalse(does_Contain_B('abc', 'def', 3))

    def test_different_strings_with_different_lengths(self):
        self.assertFalse(does_Contain_B('abc', 'def', 2))

    def test_empty_strings(self):
        self.assertFalse(does_Contain_B('', 'abc', 1))
        self.assertFalse(does_Contain_B('abc', '', 1))

    def test_negative_step(self):
        self.assertFalse(does_Contain_B('abc', 'def', -1))

    def test_zero_step(self):
        self.assertFalse(does_Contain_B('abc', 'def', 0))
