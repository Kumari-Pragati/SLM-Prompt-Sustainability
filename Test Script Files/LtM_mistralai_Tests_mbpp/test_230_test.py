import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_simple_replacement(self):
        self.assertEqual(replace_blank("Hello World", "_"), "Hello_World")
        self.assertEqual(replace_blank("I am a test", "X"), "I am a Xt")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(replace_blank("", "_"), "")
        self.assertEqual(replace_blank("   ", "_"), "__")
        self.assertEqual(replace_blank("Hello_World", "_"), "Hello_World")
        self.assertEqual(replace_blank("Hello_World_", "_"), "Hello_World_")

    def test_complex_scenarios(self):
        self.assertEqual(replace_blank("Hello World!", "X"), "Hello X World!")
        self.assertEqual(replace_blank("Hello World!", "X", 1), "HXello World!")
        self.assertEqual(replace_blank("Hello World!", "X", 2), "Hello X World!")
        self.assertEqual(replace_blank("Hello World!", "X", 3), "Hello World X!")
