import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")
        self.assertEqual(remove_spaces("   Hello   World   "), "HelloWorld")
        self.assertEqual(remove_spaces(""), "")
        self.assertEqual(remove_spaces("Hello"), "Hello")
        self.assertEqual(remove_spaces("   "), "")

    def test_edge_cases(self):
        self.assertEqual(remove_spaces("a b c"), "abc")
        self.assertEqual(remove_spaces("a  b  c"), "abc")
        self.assertEqual(remove_spaces("a   b   c"), "abc")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            remove_spaces(None)
        with self.assertRaises(TypeError):
            remove_spaces(123)
