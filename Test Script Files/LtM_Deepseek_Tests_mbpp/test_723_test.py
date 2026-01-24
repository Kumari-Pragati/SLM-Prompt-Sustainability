import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_same_pair([1, 2, 2], [2, 1, 2]), 2)

    def test_edge_conditions(self):
        self.assertEqual(count_same_pair([], []), 0)
        self.assertEqual(count_same_pair([1], [1]), 1)
        self.assertEqual(count_same_pair([1, 2, 3], [4, 5, 6]), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_same_pair([100]*100, [100]*100), 100)
        self.assertEqual(count_same_pair([-100]*100, [-100]*100), 100)
        self.assertEqual(count_same_pair([0]*100, [0]*100), 100)

    def test_complex_cases(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), 5)
        self.assertEqual(count_same_pair([1, 2, 2, 3, 3], [2, 1, 2, 3, 3]), 4)
