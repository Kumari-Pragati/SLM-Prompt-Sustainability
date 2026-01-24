import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_first_occurrence([], 1), -1)
        self.assertEqual(find_first_occurrence([1], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 5), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_first_occurrence(None, 1)
        with self.assertRaises(TypeError):
            find_first_occurrence([1, 2, 3, 4, 5], None)
