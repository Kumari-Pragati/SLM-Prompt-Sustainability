import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 1), 3)
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 2), 1)

    def test_edge_conditions(self):
        self.assertEqual(count_pairs([], 0, 1), 0)
        self.assertEqual(count_pairs([1], 1, 0), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 0), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_pairs([1, 2, 3, 4], 4, 100), 0)
        self.assertEqual(count_pairs([100, 200, 300, 400], 4, 100), 1)

    def test_complex_cases(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 5, 1), 3)
