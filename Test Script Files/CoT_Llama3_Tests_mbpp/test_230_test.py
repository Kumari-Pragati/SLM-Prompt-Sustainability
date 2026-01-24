import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(replace_blank("Hello World", "*"), "Hello*World")

    def test_edge_cases(self):
        self.assertEqual(replace_blank("", "*"), "")
        self.assertEqual(replace_blank("Hello", "*"), "Hello")
        self.assertEqual(replace_blank("   ", "*"), "***")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            replace_blank(123, "*")
        with self.assertRaises(TypeError):
            replace_blank("Hello", None)

    def test_boundary_conditions(self):
        self.assertEqual(replace_blank("Hello World", "X"), "HelloXWorld")
        self.assertEqual(replace_blank("Hello World", ""), "Hello World")
