import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):
    def test_typical_input(self):
        result = find_character("Hello, World! 123")
        self.assertEqual(result, (["H", "O", "W", "W"], ["e", "l", "l", "o", "r", "l", "d"], ["1", "2", "3"], ["", ",", " ", "!"]))

    def test_edge_case_empty_string(self):
        result = find_character("")
        self.assertEqual(result, ((), (), (), ()))

    def test_edge_case_single_character(self):
        result = find_character("A")
        self.assertEqual(result, (["A"], ["a"], [], [""]))

    def test_edge_case_all_uppercase(self):
        result = find_character("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(result, (list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [], [], []))

    def test_edge_case_all_lowercase(self):
        result = find_character("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(result, ((), list("abcdefghijklmnopqrstuvwxyz"), [], []))

    def test_edge_case_all_numerical(self):
        result = find_character("0123456789")
        self.assertEqual(result, ((), (), list("0123456789"), []))

    def test_edge_case_all_special(self):
        result = find_character(",.!?")
        self.assertEqual(result, ((), (), (), [",", ".", "!", "?"]))

    def test_edge_case_mixed_input(self):
        result = find_character("Hello, World! 123,.!?")
        self.assertEqual(result, (["H", "O", "W", "W"], ["e", "l", "l", "o", "r", "l", "d"], ["1", "2", "3"], [",", ".", "!", "?"]))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            find_character(123)
