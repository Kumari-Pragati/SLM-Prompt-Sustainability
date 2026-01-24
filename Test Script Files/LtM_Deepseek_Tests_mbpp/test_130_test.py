import unittest
from mbpp_130_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), (3, 3))

    def test_edge_boundary_conditions(self):
        self.assertEqual(max_occurrences([]), None)
        self.assertEqual(max_occurrences([1]), (1, 1))
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), (4, 4))

    def test_complex_scenarios(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]), (5, 5))
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]), (1, 1))
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), (4, 4))
