import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 2), "Hello: world:")

    def test_boundary_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 10), "Hello: world:")

    def test_edge_case(self):
        self.assertEqual(replace_max_specialchar("No special characters here", 0), "No special characters here")
        self.assertEqual(replace_max_specialchar("Only one special character,.", 1), "Only one special character,:")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar("Invalid input", "two")
        with self.assertRaises(ValueError):
            replace_max_specialchar("Invalid input", -1)
