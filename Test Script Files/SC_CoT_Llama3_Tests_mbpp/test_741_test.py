import unittest
from mbpp_741_code import all_Characters_Same

class TestAll_Characters_Same(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(all_Characters_Same("aaaaaa"))
        self.assertTrue(all_Characters_Same("111111"))
        self.assertTrue(all_Characters_Same("eeeeee"))

    def test_edge_cases(self):
        self.assertTrue(all_Characters_Same("a"))
        self.assertTrue(all_Characters_Same("b"))
        self.assertTrue(all_Characters_Same("c"))

    def test_boundary_cases(self):
        self.assertTrue(all_Characters_Same("abcdef"))
        self.assertTrue(all_Characters_Same("abcabc"))
        self.assertTrue(all_Characters_Same("aabbcc"))

    def test_special_cases(self):
        self.assertFalse(all_Characters_Same("ababab"))
        self.assertFalse(all_Characters_Same("abcde"))
        self.assertFalse(all_Characters_Same("abcdefg"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            all_Characters_Same(None)
        with self.assertRaises(TypeError):
            all_Characters_Same(123)
