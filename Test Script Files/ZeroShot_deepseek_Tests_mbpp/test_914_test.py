import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_even_length_string(self):
        self.assertFalse(is_Two_Alter('abcabc'))
        self.assertFalse(is_Two_Alter('123456'))
        self.assertFalse(is_Two_Alter('abcdabcd'))

    def test_odd_length_string(self):
        self.assertFalse(is_Two_Alter('abcabcab'))
        self.assertFalse(is_Two_Alter('1234567'))
        self.assertFalse(is_Two_Alter('abcdabcda'))

    def test_first_two_chars_same(self):
        self.assertFalse(is_Two_Alter('aabbaa'))
        self.assertFalse(is_Two_Alter('112345'))
        self.assertFalse(is_Two_Alter('abcdabcd'))

    def test_valid_strings(self):
        self.assertTrue(is_Two_Alter('aabb'))
        self.assertTrue(is_Two_Alter('1234'))
        self.assertTrue(is_Two_Alter('abcd'))
