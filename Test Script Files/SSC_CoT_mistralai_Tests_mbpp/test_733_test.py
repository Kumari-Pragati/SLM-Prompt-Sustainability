import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_first_occurrence([5, 4, 3, 2, 1], 1), 0)
        self.assertEqual(find_first_occurrence([], 0), -1)
        self.assertEqual(find_first_occurrence([0], 0), 0)

    def test_edge_cases(self):
        self.assertEqual(find_first_occurrence([1, 1, 3, 4, 5], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 2, 3, 4, 5], 2), 1)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 3, 4, 5], 2), 2)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 2, 3, 4, 5], 2), 3)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 2, 2, 3, 4, 5], 2), 4)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 2, 2, 2, 3, 4, 5], 0), -1)
        self.assertEqual(find_first_occurrence([1, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5], 6), -1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_first_occurrence, [1, 2, 3], 0.5)
        self.assertRaises(TypeError, find_first_occurrence, [1, 2, 3], "a")
        self.assertRaises(ValueError, find_first_occurrence, [], None)
        self.assertRaises(ValueError, find_first_occurrence, [], "")
