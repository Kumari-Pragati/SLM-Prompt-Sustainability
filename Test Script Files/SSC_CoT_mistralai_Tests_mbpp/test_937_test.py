import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_char("hello"), "l")
        self.assertEqual(max_char("Python"), "o")
        self.assertEqual(max_char("World"), "l")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_char("A"), "A")
        self.assertEqual(max_char("aa"), "a")
        self.assertEqual(max_char("AAAA"), "A")
        self.assertEqual(max_char(""), "")
        self.assertEqual(max_char("abcdefghijklmnopqrstuvwxyz"), "z")
        self.assertEqual(max_char("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "Z")
        self.assertEqual(max_char("1234567890"), "0")
        self.assertEqual(max_char("!@#$%^&*()_+-=[]{};':\"|,.<>/? "), " ")

    def test_special_or_corner_cases(self):
        self.assertEqual(max_char("Hello, World!"), "!")
        self.assertEqual(max_char("123_456"), "_")
        self.assertEqual(max_char("H1llo"), "1")
        self.assertEqual(max_char("H1llo!"), "!")
        self.assertEqual(max_char("H1llo@"), "@")
