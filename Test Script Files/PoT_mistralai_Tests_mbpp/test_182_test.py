import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_character(''), ([], [], [], []))

    def test_only_uppercase(self):
        self.assertEqual(find_character('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], [], [], ['!', '?']))

    def test_only_lowercase(self):
        self.assertEqual(find_character('abcdefghijklmnopqrstuvwxyz'), ([], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], [], ['.', ',']))

    def test_only_numbers(self):
        self.assertEqual(find_character('1234567890'), ([], [], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], []))

    def test_only_special_characters(self):
        self.assertEqual(find_character(', .!?'), ([], [], [], ['', ',', '.', '!', '?']))

    def test_mixed_case(self):
        self.assertEqual(find_character('A1b2c3d4E5F6G7H8I9'), (['A', 'E', 'F'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['1', '2', '3'], ['.', ',']))

    def test_long_string(self):
        self.assertEqual(find_character('A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0U1V2W3X4Y5Z6').__len__(), 4)

    def test_string_with_only_special_characters(self):
        self.assertEqual(find_character(',,.,!,?,').__len__(), 5)
