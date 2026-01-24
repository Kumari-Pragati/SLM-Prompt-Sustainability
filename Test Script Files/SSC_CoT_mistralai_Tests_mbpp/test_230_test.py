import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(replace_blank("Hello World", "_"), "Hello_World")

    def test_edge_input(self):
        self.assertEqual(replace_blank("", "_"), "")
        self.assertEqual(replace_blank("   ", "_"), "__")
        self.assertEqual(replace_blank("Hello_World", "_"), "Hello_World")

    def test_boundary_input(self):
        self.assertEqual(replace_blank("Hello ", "_"), "Hello_")
        self.assertEqual(replace_blank("Hello_", "_"), "Hello")
        self.assertEqual(replace_blank("Hello_World", "_"), "Hello_World")
        self.assertEqual(replace_blank("Hello_World_", "_"), "Hello_World")

    def test_invalid_input(self):
        self.assertRaises(TypeError, replace_blank, 1, "_")
        self.assertRaises(TypeError, replace_blank, "Hello", 1)
