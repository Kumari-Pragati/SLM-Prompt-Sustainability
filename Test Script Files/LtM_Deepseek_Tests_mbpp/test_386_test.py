import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(swap_count("[]"), 0)
        self.assertEqual(swap_count("[[]]"), 0)
        self.assertEqual(swap_count("[[[]]]"), 0)

    def test_edge_conditions(self):
        self.assertEqual(swap_count(""), 0)
        self.assertEqual(swap_count("["), 0)
        self.assertEqual(swap_count("]"), 0)

    def test_complex_cases(self):
        self.assertEqual(swap_count("[[]][][]"), 0)
        self.assertEqual(swap_count("[[[][]]]"), 0)
        self.assertEqual(swap_count("[][[[]]][][]"), 0)
        self.assertEqual(swap_count("[[[[[[[]]]]]]]"), 0)

    def test_imbalance_cases(self):
        self.assertEqual(swap_count("[]["), 1)
        self.assertEqual(swap_count("[[]]][["), 2)
        self.assertEqual(swap_count("[[[]]]][["), 2)
        self.assertEqual(swap_count("[[[]]]][[[]]"), 3)
