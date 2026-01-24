import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_empty_string(self):
        """Tests if an empty string returns expected results"""
        result = find_character("")
        self.assertEqual(result, ([], [], [], []))

    def test_only_uppercase(self):
        """Tests if a string with only uppercase characters returns expected results"""
        result = find_character("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(result, (["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], [], [], [" ", "!", "."]))

    def test_only_lowercase(self):
        """Tests if a string with only lowercase characters returns expected results"""
        result = find_character("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(result, ([], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], [], [" ", "!", ".", ",", "?"]))

    def test_only_numbers(self):
        """Tests if a string with only numbers returns expected results"""
        result = find_character("1234567890")
        self.assertEqual(result, ([], [], ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], []))

    def test_only_special_characters(self):
        """Tests if a string with only special characters returns expected results"""
        result = find_character(" ,.!? ")
        self.assertEqual(result, ([], [], [], [" ", ",", ".", "!", "?"]))

    def test_mixed_case(self):
        """Tests if a string with mixed case characters returns expected results"""
        result = find_character("AbCdEfGhIjKlMnOpQrStUvWxYz1234567890, .!?")
        expected = (["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], [" ", ",", ".", "!", "?"])
        self.assertEqual(result, expected)

    def test_long_string(self):
        """Tests if a long string returns expected results"""
        result = find_character("a" * 100 + "B" * 100 + "1" * 100 + "2" * 100 + "3" * 100)
        expected = (["a"] * 100 + ["B"] * 100, ["a"] * 100, ["1"] * 100 + ["2"] * 100, [" "] * 200)
        self.assertEqual(result, expected)

    def test_string_with_only_one_character(self):
        """Tests if a string with only one character returns expected results"""
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef