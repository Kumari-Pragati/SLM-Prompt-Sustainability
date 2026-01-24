import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):
    def test_true_concatenation(self):
        self.assertTrue(check_Concat("abc", "abc"))

    def test_false_concatenation(self):
        self.assertFalse(check_Concat("abcd", "abc"))

    def test_concatenation_with_zero_length(self):
        self.assertFalse(check_Concat("", "abc"))

    def test_concatenation_with_empty_string(self):
        self.assertFalse(check_Concat("abc", ""))

    def test_concatenation_with_single_character(self):
        self.assertTrue(check_Concat("a", "a"))

    def test_concatenation_with_long_string(self):
        self.assertTrue(check_Concat("abcdefghijklmnopqrstuvwxyz", "abc"))

    def test_concatenation_with_non_string_input(self):
        with self.assertRaises(TypeError):
            check_Concat(123, "abc")

    def test_concatenation_with_non_string_input2(self):
        with self.assertRaises(TypeError):
            check_Concat("abc", 123)
