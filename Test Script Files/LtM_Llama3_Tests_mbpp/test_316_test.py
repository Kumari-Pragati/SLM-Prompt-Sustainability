import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 3), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_last_occurrence([], 1), -1)
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_last_occurrence([1, 2, 3, 4, 5], 0), -1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_last_occurrence("abc", 1)
        with self.assertRaises(TypeError):
            find_last_occurrence([1, 2, 3], "abc")
