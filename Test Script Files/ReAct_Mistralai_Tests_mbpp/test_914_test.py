import unittest
from914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_Two_Alter(""))

    def test_single_character(self):
        self.assertFalse(is_Two_Alter("a"))

    def test_two_characters(self):
        self.assertFalse(is_Two_Alter("ab"))

    def test_three_characters(self):
        self.assertTrue(is_Two_Alter("abc"))
        self.assertTrue(is_Two_Alter("def"))
        self.assertFalse(is_Two_Alter("abcdef"))

    def test_four_characters(self):
        self.assertTrue(is_Two_Alter("abcd"))
        self.assertFalse(is_Two_Alter("abab"))
        self.assertFalse(is_Two_Alter("abcdabcd"))

    def test_longer_strings(self):
        for i in range(5, 10):
            self.assertTrue(is_Two_Alter("a" * i))
            self.assertFalse(is_Two_Alter("a" * i + "a"))
            self.assertFalse(is_Two_Alter("a" * i + "b" + "a" * (i - 1)))

    def test_special_characters(self):
        self.assertTrue(is_Two_Alter("A1B2C3"))
        self.assertFalse(is_Two_Alter("A1B1C3"))
        self.assertFalse(is_Two_Alter("A1B2C1"))
