import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_character(""), ([], [], [], []))

    def test_string_with_uppercase_characters(self):
        self.assertEqual(find_character("HelloWorld"),(["H", "W"], ["o", "o"], [""], [""]))

    def test_string_with_lowercase_characters(self):
        self.assertEqual(find_character("hello world"),([""], ["o", "o"], [""], [""]))

    def test_string_with_numerical_characters(self):
        self.assertEqual(find_character("123"),([""], [], ["1", "2", "3"], [""]))

    def test_string_with_special_characters(self):
        self.assertEqual(find_character("Hello, World!"),([""], ["o", "o"], [""], [",", " ", "!"]))

    def test_string_with_all_types_of_characters(self):
        self.assertEqual(find_character("Hello123, World!"),(["H", "W"], ["o", "o"], ["1", "2", "3"], [",", " ", "!"]))
