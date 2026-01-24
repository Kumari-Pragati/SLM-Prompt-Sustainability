import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(remove_spaces("Hello World"), "Hello World")

    def test_edge_cases(self):
        self.assertEqual(remove_spaces(""), "")
        self.assertEqual(remove_spaces("Hello "), "Hello")
        self.assertEqual(remove_spaces("Hello World "), "Hello World")
        self.assertEqual(remove_spaces("Hello\tWorld"), "Hello World")

    def test_boundary_cases(self):
        self.assertEqual(remove_spaces("Hell oWorld"), "Hell oWorld")
        self.assertEqual(remove_spaces("Hell o World"), "Hell o World")
        self.assertEqual(remove_spaces("Hell o\tWorld"), "Hell o World")

    def test_special_cases(self):
        self.assertEqual(remove_spaces("He ll o W orld"), "He ll o W orld")
        self.assertEqual(remove_spaces("He ll o W orld!"), "He ll o W orld!")
        self.assertEqual(remove_spaces("He ll o W orld\n"), "He ll o W orld")

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_spaces, 123)
        self.assertRaises(TypeError, remove_spaces, None)
