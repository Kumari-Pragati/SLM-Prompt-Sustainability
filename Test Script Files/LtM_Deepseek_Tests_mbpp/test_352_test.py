import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(unique_Characters("abc"))
        self.assertTrue(unique_Characters("123"))
        self.assertTrue(unique_Characters(""))

    def test_edge_conditions(self):
        self.assertTrue(unique_Characters("a"))
        self.assertTrue(unique_Characters("ab"))
        self.assertFalse(unique_Characters("aa"))
        self.assertFalse(unique_Characters("aba"))

    def test_complex_cases(self):
        self.assertFalse(unique_Characters("abcba"))
        self.assertFalse(unique_Characters("abab"))
        self.assertTrue(unique_Characters("abcdefg"))
