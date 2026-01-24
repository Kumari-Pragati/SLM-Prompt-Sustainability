import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 2), "Hello:World!")

    def test_boundary_condition(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 10), "Hello:World!")

    def test_edge_condition(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 0), "Hello, World!")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar("Hello, World!", "two")
