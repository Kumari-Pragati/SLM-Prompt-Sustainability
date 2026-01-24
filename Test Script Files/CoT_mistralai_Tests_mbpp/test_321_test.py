import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_demlo(""), "")

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(find_demlo(char), str(1) + str(len(char)))

    def test_multiple_characters_string(self):
        for string in "abcd", "abcdefg", "1234567890":
            self.assertEqual(find_demlo(string), find_demlo(str(len(string))[::-1]))

    def test_negative_string(self):
        self.assertRaises(ValueError, find_demlo, "-123")

    def test_zero_string(self):
        self.assertRaises(ValueError, find_demlo, "0")

    def test_special_characters_string(self):
        self.assertRaises(ValueError, find_demlo, "!@#$%^&*()_+-=[]{}|;:'\",.<>?/")
