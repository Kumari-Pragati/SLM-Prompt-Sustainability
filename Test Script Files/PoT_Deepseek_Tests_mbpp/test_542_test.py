import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(fill_spaces("Hello, world."), "Hello:world:")
        self.assertEqual(fill_spaces("Python is great."), "Python:is:great:")

    def test_edge_cases(self):
        self.assertEqual(fill_spaces(""), "")
        self.assertEqual(fill_spaces("No spaces here"), "No spaces here")

    def test_boundary_conditions(self):
        self.assertEqual(fill_spaces(" "), ":")
        self.assertEqual(fill_spaces("., "), ":")

    def test_corner_cases(self):
        self.assertEqual(fill_spaces("., "), ":")
        self.assertEqual(fill_spaces("Multiple   spaces"), "Multiple:spaces")
        self.assertEqual(fill_spaces("No change needed"), "No change needed")
