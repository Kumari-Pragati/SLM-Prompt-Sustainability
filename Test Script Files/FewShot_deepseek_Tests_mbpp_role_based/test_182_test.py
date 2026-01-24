import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):
    def test_typical_use_case(self):
        string = "HelloWorld123!?"
        result = find_character(string)
        self.assertEqual(result, (['H', 'W', 'O', 'R', 'L', 'D'], ['e', 'l', 'o', 'r', 'l', 'd'], ['1', '2', '3'], [',', '.', '!', '?']))

    def test_empty_string(self):
        string = ""
        result = find_character(string)
        self.assertEqual(result, ([], [], [], []))

    def test_string_with_only_uppercase(self):
        string = "HELLO"
        result = find_character(string)
        self.assertEqual(result, (['H', 'E', 'L', 'L', 'O'], [], [], []))

    def test_string_with_only_lowercase(self):
        string = "hello"
        result = find_character(string)
        self.assertEqual(result, ([], ['h', 'e', 'l', 'l', 'o'], [], []))

    def test_string_with_only_numbers(self):
        string = "123"
        result = find_character(string)
        self.assertEqual(result, ([], [], ['1', '2', '3'], []))

    def test_string_with_only_special_characters(self):
        string = ", .!? "
        result = find_character(string)
        self.assertEqual(result, ([], [], [], [',', '.', '!', '?', ' ']))

    def test_string_with_no_characters(self):
        string = "1234567890"
        result = find_character(string)
        self.assertEqual(result, ([], [], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], []))
