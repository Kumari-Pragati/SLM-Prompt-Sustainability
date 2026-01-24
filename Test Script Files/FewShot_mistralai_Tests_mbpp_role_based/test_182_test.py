import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_character(''), ([], [], [], []))

    def test_all_uppercase(self):
        self.assertEqual(find_character('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], [], [], [' ', ',', '.', '!', '?']))

    def test_all_lowercase(self):
        self.assertEqual(find_character('abcdefghijklmnopqrstuvwxyz'), ([], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], [], [' ', ',', '.', '!', '?']))

    def test_mixed_case(self):
        self.assertEqual(find_character('AbCdEfGhIjKlMnOpQrStUvWxYz'), (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], [], [' ', ',', '.', '!', '?']))

    def test_special_characters(self):
        self.assertEqual(find_character('Hello, World!'), ([], [], [], ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']))

    def test_numbers(self):
        self.assertEqual(find_character('1234567890'), ([], [], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], []))
