import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_spaces("Hello World"), "Hello World")
        self.assertEqual(remove_spaces("A B C"), "A B C")
        self.assertEqual(remove_spaces("   Hello World   "), "Hello World")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_spaces("A "), "A ")
        self.assertEqual(remove_spaces(" "), "")

    def test_edge_case_multiple_spaces_start_end(self):
        self.assertEqual(remove_spaces("   "), "")
        self.assertEqual(remove_spaces(" Hello World "), "Hello World")

    def test_edge_case_multiple_spaces_middle(self):
        self.assertEqual(remove_spaces("A   B   C"), "A B C")
        self.assertEqual(remove_spaces("A    B    C"), "A B C")
