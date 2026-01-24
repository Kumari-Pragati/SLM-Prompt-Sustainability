import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(find_substring("Hello World", "World"))
        self.assertTrue(find_substring("Python Programming", "Programming"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(find_substring("", ""))
        self.assertFalse(find_substring("", "World"))
        self.assertFalse(find_substring("World", ""))
        self.assertTrue(find_substring("Hello World", "H"))
        self.assertTrue(find_substring("Hello World", "o"))
        self.assertTrue(find_substring("Hello World", "lo"))
        self.assertFalse(find_substring("Hello World", "X"))
        self.assertTrue(find_substring("Hello World", "ll"))

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_substring, 123, "World")
        self.assertRaises(TypeError, find_substring, "Hello", 123)
