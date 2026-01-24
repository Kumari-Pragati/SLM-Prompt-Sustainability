import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(fill_spaces("Hello World"), "Hello:World")
        self.assertEqual(fill_spaces("Python is fun"), "Python:is:fun")
        self.assertEqual(fill_spaces("   Hello   "), "Hello")

    def test_edge_cases(self):
        self.assertEqual(fill_spaces(""), "")
        self.assertEqual(fill_spaces("Hello"), "Hello")
        self.assertEqual(fill_spaces("Hello,World"), "Hello:World")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            fill_spaces(123)
        with self.assertRaises(TypeError):
            fill_spaces(None)
