import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_simple_string(self):
        self.assertListEqual(find_character("HelloWorld123!"),
                              (['H', 'L', 'O', 'W', 'R', 'D', '1', '2', '3'],
                               ['h', 'l', 'o', 'w', 'r', 'd', '1', '2', '3'],
                               ['1', '2', '3'], ['.', ',', '!']))

    def test_empty_string(self):
        self.assertListEqual(find_character(""), ([], [], [], []))

    def test_all_uppercase(self):
        self.assertListEqual(find_character("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                              (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                               [], [], [], []))

    def test_all_lowercase(self):
        self.assertListEqual(find_character("abcdefghijklmnopqrstuvwxyz"),
                              ([], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], [], []))

    def test_all_numbers(self):
        self.assertListEqual(find_character("1234567890"),
                              ([], [], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], []))

    def test_all_special_characters(self):
        self.assertListEqual(find_character(".,!?@#$%^&*()_+-="),
                              ([], [], [], ['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']))

    def test_mixed_case(self):
        self.assertListEqual(find_character("HeLlOwOrLd123!"),
                              (['H', 'e', 'L', 'l', 'o', 'w', 'O', 'r', 'L', 'd', '1', '2', '3'],
                               ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '1', '2', '3'],
                               ['1', '2', '3'], ['!', '.', ',']))
