import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 2, 1], 2), 3)
        self.assertEqual(find_last_occurrence([4, 5, 6, 7, 8], 8), 4)
        self.assertEqual(find_last_occurrence([], 0), -1)
        self.assertEqual(find_last_occurrence([0], 0), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1, 1], 1), 1)
        self.assertEqual(find_last_occurrence([1, 2, 1], 1), 3)
        self.assertEqual(find_last_occurrence([1, 2, 1, 2, 1], 2), 4)
        self.assertEqual(find_last_occurrence([1, 2, 1, 2, 1], 3), -1)
        self.assertEqual(find_last_occurrence([1, 2, 1, 2, 1], 0), -1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_last_occurrence, [1, 2, 3], 0.5)
        self.assertRaises(TypeError, find_last_occurrence, [1, 2, 3], "x")
