import unittest
from mbpp_150_code import does_Contain_B

class TestDoesContainB(unittest.TestCase):
    def test_equal_strings(self):
        self.assertTrue(does_Contain_B('a', 'a', 1))
        self.assertTrue(does_Contain_B('A', 'a', 1))
        self.assertTrue(does_Contain_B('a', 'A', 1))

    def test_different_strings(self):
        self.assertFalse(does_Contain_B('a', 'b', 1))
        self.assertFalse(does_Contain_B('a', 'c', 1))
        self.assertFalse(does_Contain_B('b', 'a', 1))

    def test_same_string_with_different_case_and_c(self):
        self.assertTrue(does_Contain_B('a', 'a', 2))
        self.assertTrue(does_Contain_B('a', 'a', -1))
        self.assertTrue(does_Contain_B('a', 'a', 3))

    def test_different_strings_with_same_case_and_c(self):
        self.assertFalse(does_Contain_B('a', 'b', 2))
        self.assertFalse(does_Contain_B('a', 'b', -1))
        self.assertFalse(does_Contain_B('a', 'b', 3))

    def test_same_string_with_different_case(self):
        self.assertTrue(does_Contain_B('a', 'A', 1))
        self.assertTrue(does_Contain_B('A', 'a', 1))

    def test_empty_strings(self):
        self.assertFalse(does_Contain_B('', '', 1))
        self.assertFalse(does_Contain_B('', 'a', 1))
        self.assertFalse(does_Contain_B('a', '', 1))
