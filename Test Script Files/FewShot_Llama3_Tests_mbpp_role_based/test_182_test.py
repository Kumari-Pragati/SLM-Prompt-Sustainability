import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):
    def test_typical_use_case(self):
        string = "Hello, World! 123"
        result = find_character(string)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], ['H', 'W'])
        self.assertEqual(result[1], ['o', 'o', 'r', 'l', 'd'])
        self.assertEqual(result[2], ['1', '2', '3'])
        self.assertEqual(result[3], [',', '.', '!',''])

    def test_empty_string(self):
        string = ""
        result = find_character(string)
        self.assertEqual(result, ([], [], [], []))

    def test_no_uppercase_characters(self):
        string = "hello world 123"
        result = find_character(string)
        self.assertEqual(result[0], [])

    def test_no_lowercase_characters(self):
        string = "HELLO WORLD 123"
        result = find_character(string)
        self.assertEqual(result[1], [])

    def test_no_numerical_characters(self):
        string = "Hello World,."
        result = find_character(string)
        self.assertEqual(result[2], [])

    def test_no_special_characters(self):
        string = "Hello World 123"
        result = find_character(string)
        self.assertEqual(result[3], [])

    def test_multiple_types_of_characters(self):
        string = "Hello, World! 123,."
        result = find_character(string)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], ['H', 'W'])
        self.assertEqual(result[1], ['o', 'o', 'r', 'l', 'd'])
        self.assertEqual(result[2], ['1', '2', '3'])
        self.assertEqual(result[3], [',', '.','', '!'])
