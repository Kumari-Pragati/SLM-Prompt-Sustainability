import unittest
from mbpp_741_code import all_Characters_Same

class TestAll_Characters_Same(unittest.TestCase):

    def test_all_Characters_Same(self):
        self.assertTrue(all_Characters_Same("aaaa"))
        self.assertTrue(all_Characters_Same("aaab"))
        self.assertFalse(all_Characters_Same("abc"))
        self.assertFalse(all_Characters_Same("aabb"))
        self.assertTrue(all_Characters_Same("aaaaaa"))
        self.assertFalse(all_Characters_Same("aabbcc"))
        self.assertTrue(all_Characters_Same("aaaaaaa"))
        self.assertFalse(all_Characters_Same("aabbccdd"))

    def test_empty_string(self):
        self.assertTrue(all_Characters_Same(""))

    def test_single_character_string(self):
        self.assertTrue(all_Characters_Same("a"))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            all_Characters_Same(123)
