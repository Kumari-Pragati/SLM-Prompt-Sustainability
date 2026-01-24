import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_three_characters(self):
        self.assertTrue(is_Two_Alter("abc"))

    def test_four_characters_same_first_and_second(self):
        self.assertFalse(is_Two_Alter("abcd"))

    def test_four_characters_different_first_and_third(self):
        self.assertTrue(is_Two_Alter("abcd"))

    def test_five_characters_same_first_and_second(self):
        self.assertFalse(is_Two_Alter("abcde"))

    def test_five_characters_different_first_and_third(self):
        self.assertTrue(is_Two_Alter("abcdx"))

    def test_empty_string(self):
        self.assertFalse(is_Two_Alter(""))

    def test_single_character(self):
        self.assertFalse(is_Two_Alter("a"))

    def test_two_characters(self):
        self.assertFalse(is_Two_Alter("ab"))
