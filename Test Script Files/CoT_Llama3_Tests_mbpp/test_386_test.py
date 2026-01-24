import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(swap_count(""), 0)

    def test_single_bracket(self):
        self.assertEqual(swap_count("["), 0)
        self.assertEqual(swap_count("]"), 0)

    def test_balanced_brackets(self):
        self.assertEqual(swap_count("[]"), 0)
        self.assertEqual(swap_count("[][]"), 0)

    def test_unbalanced_brackets(self):
        self.assertEqual(swap_count("["), 1)
        self.assertEqual(swap_count("]"), 1)
        self.assertEqual(swap_count("][["), 2)
        self.assertEqual(swap_count("][[]"), 2)

    def test_multiple_brackets(self):
        self.assertEqual(swap_count("[][]"), 0)
        self.assertEqual(swap_count("[][][]"), 0)
        self.assertEqual(swap_count("[][][][]"), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            swap_count(None)
        with self.assertRaises(TypeError):
            swap_count(123)
