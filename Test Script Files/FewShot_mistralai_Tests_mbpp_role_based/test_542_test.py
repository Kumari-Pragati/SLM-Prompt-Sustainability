import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_simple_text(self):
        self.assertEqual(fill_spaces("Hello, World."), "Hello:World:")

    def test_empty_text(self):
        self.assertEqual(fill_spaces(""), "")

    def test_text_with_only_spaces(self):
        self.assertEqual(fill_spaces("   "), ":")

    def test_text_with_only_commas(self):
        self.assertEqual(fill_spaces("a,b,c"), "a:b:c")

    def test_text_with_only_periods(self):
        self.assertEqual(fill_spaces("a.b.c"), "a:b:c")

    def test_text_with_spaces_commas_and_periods(self):
        self.assertEqual(fill_spaces("a, b. c"), "a:b:c")
