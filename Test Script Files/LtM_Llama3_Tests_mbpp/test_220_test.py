import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 1), "Hello:, World!")
        self.assertEqual(replace_max_specialchar("This is a test", 2), "This is:a test")
        self.assertEqual(replace_max_specialchar("Python is awesome", 3), "Python is:awesome")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(replace_max_specialchar("", 1), "")
        self.assertEqual(replace_max_specialchar("Hello, World!", 0), "Hello, World!")
        self.assertEqual(replace_max_specialchar("This is a test", 5), "This is:a test")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar(123, 1)
        with self.assertRaises(TypeError):
            replace_max_specialchar("Hello, World!", "abc")
