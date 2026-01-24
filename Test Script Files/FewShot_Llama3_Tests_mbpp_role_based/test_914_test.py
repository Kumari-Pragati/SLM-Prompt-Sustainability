import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_true_positive(self):
        self.assertTrue(is_Two_Alter("abcde"))

    def test_true_negative(self):
        self.assertTrue(is_Two_Alter("aabbcc"))

    def test_false_positive(self):
        self.assertFalse(is_Two_Alter("abcdef"))

    def test_false_negative(self):
        self.assertFalse(is_Two_Alter("aaabbc"))

    def test_empty_string(self):
        self.assertFalse(is_Two_Alter(""))

    def test_single_character_string(self):
        self.assertFalse(is_Two_Alter("a"))

    def test_two_character_string(self):
        self.assertFalse(is_Two_Alter("ab"))

    def test_three_character_string(self):
        self.assertTrue(is_Two_Alter("abc"))
