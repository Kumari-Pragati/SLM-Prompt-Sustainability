import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(replace_specialchar("Hello, World."), "Hello:World:")
        self.assertEqual(replace_specialchar("Python is great."), "Python is great.")
        self.assertEqual(replace_specialchar("Replace all, Replace some."), "Replace all: Replace some.")

    def test_edge_cases(self):
        self.assertEqual(replace_specialchar(""), "")
        self.assertEqual(replace_specialchar("No special characters."), "No special characters.")

    def test_corner_cases(self):
        self.assertEqual(replace_specialchar("., "), ":")
        self.assertEqual(replace_specialchar("Special characters: ., "), "Special characters: :")
