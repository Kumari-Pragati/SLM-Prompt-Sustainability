import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find_character("HelloWorld123"), 
                         (['H', 'W'], ['e', 'o', 'l', 'l', 'o', 'r', 'd'], ['1', '2', '3'], []))

    def test_edge_cases(self):
        self.assertEqual(find_character(""), ([], [], [], []))
        self.assertEqual(find_character("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 
                         (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], [], [], []))
        self.assertEqual(find_character("abcdefghijklmnopqrstuvwxyz"), 
                         ([], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], [], []))
        self.assertEqual(find_character("1234567890"), ([], [], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], []))

    def test_corner_cases(self):
        self.assertEqual(find_character("!@#$%^&*()"), ([], [], [], ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_character(123)
        with self.assertRaises(TypeError):
            find_character(None)
        with self.assertRaises(TypeError):
            find_character(["Hello", "World"])
