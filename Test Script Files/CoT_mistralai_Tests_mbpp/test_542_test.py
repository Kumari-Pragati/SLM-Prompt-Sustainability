import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(fill_spaces("Hello, World."), "Hello:World:")
        self.assertEqual(fill_spaces("Hello, World, It's a nice day."), "Hello:World:It's:a:nice:day:.")

    def test_edge_case_single_space(self):
        self.assertEqual(fill_spaces("Hello "), "Hello:")
        self.assertEqual(fill_spaces(" Hello"), "Hello:")
        self.assertEqual(fill_spaces(" World"), ":World:")

    def test_edge_case_no_spaces(self):
        self.assertEqual(fill_spaces("HelloWorld"), "HelloWorld")
        self.assertEqual(fill_spaces("Hello,World"), "Hello:World")

    def test_edge_case_only_punctuation(self):
        self.assertEqual(fill_spaces(",."), ":")
        self.assertEqual(fill_spaces("!?"), ":")
        self.assertEqual(fill_spaces(".,!?"), ":")

    def test_invalid_input(self):
        self.assertRaises(TypeError, fill_spaces, 123)
        self.assertRaises(TypeError, fill_spaces, None)
        self.assertRaises(TypeError, fill_spaces, [])
        self.assertRaises(TypeError, fill_spaces, {})
