import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(fill_spaces("Hello, world."), "Hello:world:")

    def test_edge_case(self):
        self.assertEqual(fill_spaces(""), "")

    def test_special_case(self):
        self.assertEqual(fill_spaces("No spaces here"), "No spaces here")
        self.assertEqual(fill_spaces("123456"), "123456")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fill_spaces(123456)
