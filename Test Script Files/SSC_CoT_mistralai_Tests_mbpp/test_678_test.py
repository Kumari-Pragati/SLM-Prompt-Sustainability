import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(remove_spaces(""), "")
        self.assertEqual(remove_spaces("Hello"), "Hello")
        self.assertEqual(remove_spaces("Hello World!"), "HelloWorld!")
        self.assertEqual(remove_spaces("  Hello World  "), "HelloWorld")

    def test_special_input(self):
        self.assertEqual(remove_spaces("Hello-World"), "HelloWorld")
        self.assertEqual(remove_spaces("Hello_World"), "HelloWorld")
        self.assertEqual(remove_spaces("Hello123World"), "Hello123World")

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_spaces, 123)
        self.assertRaises(TypeError, remove_spaces, None)
        self.assertRaises(TypeError, remove_spaces, [])
