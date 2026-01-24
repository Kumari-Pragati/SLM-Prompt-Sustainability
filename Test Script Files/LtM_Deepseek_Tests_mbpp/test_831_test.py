import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Pairs([1, 2, 3, 2, 1], 5), 2)
        self.assertEqual(count_Pairs([1, 1, 1, 1, 1], 5), 10)
        self.assertEqual(count_Pairs([5, 5, 5, 5, 5], 5), 10)

    def test_edge_conditions(self):
        self.assertEqual(count_Pairs([], 0), 0)
        self.assertEqual(count_Pairs([1], 1), 0)
        self.assertEqual(count_Pairs([1, 2], 2), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3], 5), 2)
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3], 5), 4)

    def test_complex_cases(self):
        self.assertEqual(count_Pairs([1, 2, 2, 3, 3, 4, 4, 5, 5], 9), 4)
        self.assertEqual(count_Pairs([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5], 13), 6)
