import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_last_occurrence(['a', 'b', 'c', 'd', 'e'], 'c'), 2)

    def test_edge_conditions(self):
        self.assertEqual(find_last_occurrence([], 1), -1)
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_boundary_conditions(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 3, 4, 5], 3), 4)
        self.assertEqual(find_last_occurrence([1, 2, 2, 3, 4, 5], 2), 3)

    def test_complex_cases(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 3, 3, 4, 5], 3), 5)
        self.assertEqual(find_last_occurrence([1, 2, 2, 2, 3, 4, 5], 2), 4)
