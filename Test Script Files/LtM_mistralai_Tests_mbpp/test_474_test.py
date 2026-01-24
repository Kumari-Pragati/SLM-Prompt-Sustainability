import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_simple_replace(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "HeLo")
        self.assertEqual(replace_char("World", "r", "R"), "WoLd")

    def test_edge_cases(self):
        self.assertEqual(replace_char("", "a", "b"), "")
        self.assertEqual(replace_char("A", "A", "B"), "B")
        self.assertEqual(replace_char("Aaa", "a", "B"), "Baa")
        self.assertEqual(replace_char("Aaa", "z", "B"), "Aaa")

    def test_complex_cases(self):
        self.assertEqual(replace_char("Hell-o", "-", " "), "Hell o")
        self.assertEqual(replace_char("Hell0", "0", " "), "Hell")
        self.assertEqual(replace_char("Hell_o", "_", " "), "Hell o")
