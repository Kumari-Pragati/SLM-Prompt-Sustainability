import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(unique_Characters("abcde"))

    def test_edge_case(self):
        self.assertFalse(unique_Characters("aabbcc"))

    def test_edge_case2(self):
        self.assertFalse(unique_Characters("aaabbc"))

    def test_edge_case3(self):
        self.assertTrue(unique_Characters("abcdefghijklmnopqrstuvwxyz"))

    def test_edge_case4(self):
        self.assertTrue(unique_Characters(""))

    def test_edge_case5(self):
        self.assertFalse(unique_Characters("aabbccdd"))

    def test_edge_case6(self):
        self.assertFalse(unique_Characters("aabbccddaa"))

    def test_edge_case7(self):
        self.assertTrue(unique_Characters("a"))

    def test_edge_case8(self):
        self.assertTrue(unique_Characters("ab"))

    def test_edge_case9(self):
        self.assertFalse(unique_Characters("aa"))

    def test_edge_case10(self):
        self.assertFalse(unique_Characters("abab"))
