import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_specialchar("Hello, World!"), "Hello:World:")

    def test_edge_condition(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_boundary_condition(self):
        self.assertEqual(replace_specialchar("A."), "A:")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_specialchar(123)
