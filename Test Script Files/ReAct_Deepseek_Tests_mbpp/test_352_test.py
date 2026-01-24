import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(unique_Characters("abcde"))
        self.assertTrue(unique_Characters("12345"))
        self.assertTrue(unique_Characters("abcd"))

    def test_edge_cases(self):
        self.assertTrue(unique_Characters(""))
        self.assertTrue(unique_Characters("a"))
        self.assertTrue(unique_Characters("ab"))

    def test_error_cases(self):
        self.assertRaises(TypeError, unique_Characters, 12345)
        self.assertRaises(TypeError, unique_Characters, ["a", "b", "c"])
