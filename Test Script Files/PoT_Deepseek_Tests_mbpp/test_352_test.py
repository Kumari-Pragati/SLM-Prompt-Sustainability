import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(unique_Characters("abcde"))
        self.assertTrue(unique_Characters("abcdefghijklmnopqrstuvwxyz"))

    def test_edge_cases(self):
        self.assertTrue(unique_Characters(""))
        self.assertTrue(unique_Characters("a"))

    def test_boundary_cases(self):
        self.assertFalse(unique_Characters("aa"))
        self.assertFalse(unique_Characters("abab"))

    def test_corner_cases(self):
        self.assertFalse(unique_Characters("abcabc"))
        self.assertFalse(unique_Characters("aabbcc"))
        self.assertFalse(unique_Characters("abcabcabc"))
