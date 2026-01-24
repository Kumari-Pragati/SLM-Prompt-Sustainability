import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_typical_case(self):
        result = find_character("Hello, World! 123")
        self.assertEqual(result, (["H", "W"], ["o", "o", "r", "l", "d"], ["1", "2", "3"], ["", ",", "!"]))

    def test_edge_case_empty_string(self):
        result = find_character("")
        self.assertEqual(result, ((), (), (), ()))

    def test_edge_case_single_character(self):
        result = find_character("a")
        self.assertEqual(result, ((), ["a"], [], [""]))

    def test_edge_case_single_digit(self):
        result = find_character("1")
        self.assertEqual(result, ((), [], ["1"], [""]))

    def test_edge_case_single_uppercase(self):
        result = find_character("A")
        self.assertEqual(result,(["A"], [], [], [""]))

    def test_edge_case_single_special_character(self):
        result = find_character(",")
        self.assertEqual(result, ((), (), [], [","]))

    def test_edge_case_multiple_characters(self):
        result = find_character("Hello, World! 123")
        self.assertEqual(result, (["H", "W"], ["o", "o", "r", "l", "d"], ["1", "2", "3"], ["", ",", "!"]))

    def test_edge_case_multiple_digits(self):
        result = find_character("123456")
        self.assertEqual(result, ((), [], ["1", "2", "3", "4", "5", "6"], [""]))

    def test_edge_case_multiple_uppercase(self):
        result = find_character("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(result, (list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [], [], [""]))

    def test_edge_case_multiple_special_characters(self):
        result = find_character("!,.,.,!")
        self.assertEqual(result, ((), (), [], [",", ".", "!"]))
