import unittest
from mbpp_741_code import all_Characters_Same

class TestAllCharactersSame(unittest.TestCase):

    def test_simple_same_characters(self):
        self.assertTrue(all_Characters_Same("aaa"))
        self.assertTrue(all_Characters_Same("bbb"))
        self.assertTrue(all_Characters_Same("ccc"))

    def test_simple_different_characters(self):
        self.assertFalse(all_Characters_Same("aaaabb"))
        self.assertFalse(all_Characters_Same("aaabbcc"))
        self.assertFalse(all_Characters_Same("abcd"))

    def test_edge_cases(self):
        self.assertTrue(all_Characters_Same(""))
        self.assertTrue(all_Characters_Same("a"))
        self.assertTrue(all_Characters_Same("aa"))

    def test_boundary_cases(self):
        self.assertTrue(all_Characters_Same("z" * 100))
        self.assertTrue(all_Characters_Same("Z" * 100))
        self.assertTrue(all_Characters_Same("0" * 100))
        self.assertTrue(all_Characters_Same("9" * 100))
