import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_length("Hello World", 5), "Hello World")

    def test_edge_case(self):
        self.assertEqual(remove_length("", 0), "")

    def test_boundary_case(self):
        self.assertEqual(remove_length("a b c d e", 1), "a b c d e")

    def test_corner_case(self):
        self.assertEqual(remove_length("1 2 3 4 5", 1), "1 2 3 4 5")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_length("Hello World", "five")
