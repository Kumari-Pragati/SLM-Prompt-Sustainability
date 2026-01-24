import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(swap_count("[]"), 0)
        self.assertEqual(swap_count("[[]]"), 0)
        self.assertEqual(swap_count("[[[]]]"), 0)
        self.assertEqual(swap_count("[[][]]"), 0)
        self.assertEqual(swap_count("[[[][]]]"), 0)
        self.assertEqual(swap_count("[[[[][]]]]"), 0)

    def test_edge_cases(self):
        self.assertEqual(swap_count("["), 0)
        self.assertEqual(swap_count("]"), 0)
        self.assertEqual(swap_count("]["), 1)
        self.assertEqual(swap_count("]["), 1)
        self.assertEqual(swap_count("]["), 1)

    def test_boundary_conditions(self):
        self.assertEqual(swap_count("][" * 10000), 10000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            swap_count(123)
        with self.assertRaises(TypeError):
            swap_count(None)
        with self.assertRaises(TypeError):
            swap_count(True)
        with self.assertRaises(TypeError):
            swap_count(["[", "]"])
