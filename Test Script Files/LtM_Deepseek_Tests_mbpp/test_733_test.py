import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 2), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_first_occurrence([], 1), -1)
        self.assertEqual(find_first_occurrence([1], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 3), 4)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 2), 1)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 3), 4)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 4), -1)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 5), -1)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3], 1), 0)
