import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")
        self.assertEqual(remove_all_spaces("   Hello   World   "), "HelloWorld")
        self.assertEqual(remove_all_spaces("This is a test"), "Thisisatest")

    def test_edge_cases(self):
        self.assertEqual(remove_all_spaces(""), "")
        self.assertEqual(remove_all_spaces("   "), "")
        self.assertEqual(remove_all_spaces("Hello"), "Hello")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            remove_all_spaces(None)
        with self.assertRaises(TypeError):
            remove_all_spaces(123)
