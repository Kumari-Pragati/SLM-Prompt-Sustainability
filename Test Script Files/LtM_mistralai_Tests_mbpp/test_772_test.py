import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_length("a b c d", 3), "a d")
        self.assertEqual(remove_length("a a a", 2), "a")
        self.assertEqual(remove_length("a a", 1), "")

    def test_edge_input(self):
        self.assertEqual(remove_length("", 3), "")
        self.assertEqual(remove_length("a", 3), "")
        self.assertEqual(remove_length("a a a", 4), "a a")
        self.assertEqual(remove_length("a a a", 1), "")

    def test_complex_input(self):
        self.assertEqual(remove_length("a b c d e f g h", 3), "a d g")
        self.assertEqual(remove_length("a a a b b b", 2), "a a b")
        self.assertEqual(remove_length("a a a b b b", 1), "b")
