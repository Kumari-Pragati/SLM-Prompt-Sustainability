import unittest
from mbpp_130_code import defaultdict
from 130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 5]), (3, 3))
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]), (4, 4))

    def test_edge_input(self):
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5]), (5, 2))
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), (5, 3))

    def test_boundary_input(self):
        self.assertEqual(max_occurrences([1]), (1, 1))
        self.assertEqual(max_occurrences([1, 1]), (1, 2))
        self.assertEqual(max_occurrences([1, 1, 1]), (1, 3))

        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), (None, None))

    def test_invalid_input(self):
        self.assertRaises(TypeError, max_occurrences, [1, 'a', 3])
        self.assertRaises(TypeError, max_occurrences, [1, 2, 3, 4, 5, 5.5])
