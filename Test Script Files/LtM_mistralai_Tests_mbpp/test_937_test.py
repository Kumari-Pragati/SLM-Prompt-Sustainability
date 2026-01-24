import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_char("hello"), "l")
        self.assertEqual(max_char("Python"), "o")
        self.assertEqual(max_char("Test"), "t")

    def test_edge_cases(self):
        self.assertEqual(max_char(""), "")
        self.assertEqual(max_char("a"), "a")
        self.assertEqual(max_char("aaa"), "a")
        self.assertEqual(max_char("Aaa"), "A")
        self.assertEqual(max_char("12345"), "5")
        self.assertEqual(max_char("!@#$%^&*()"), "*")

    def test_complex_cases(self):
        self.assertEqual(max_char("Pythons"), "s")
        self.assertEqual(max_char("PythoN"), "N")
        self.assertEqual(max_char("PythoNn"), "n")
        self.assertEqual(max_char("PythoNnN"), "N")
        self.assertEqual(max_char("PythoNnNn"), "n")
