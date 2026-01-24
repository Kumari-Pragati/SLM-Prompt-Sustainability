import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(fill_spaces("Hello World"), "Hello:World")

    def test_edge_condition_empty_string(self):
        self.assertEqual(fill_spaces(""), "")

    def test_edge_condition_single_character(self):
        self.assertEqual(fill_spaces("a"), "a")

    def test_boundary_condition_spaces(self):
        self.assertEqual(fill_spaces("Hello   World"), "Hello::World")

    def test_boundary_condition_commas(self):
        self.assertEqual(fill_spaces("Hello,World"), "Hello:World")

    def test_boundary_condition_periods(self):
        self.assertEqual(fill_spaces("Hello.World"), "Hello:World")

    def test_boundary_condition_mixed_characters(self):
        self.assertEqual(fill_spaces("Hello, World. How are you?"), "Hello:World:How:are:you:")
