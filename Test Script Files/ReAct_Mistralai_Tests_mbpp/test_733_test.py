import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_first_occurrence([], 1), -1)

    def test_single_element(self):
        self.assertEqual(find_first_occurrence([1], 1), 0)
        self.assertEqual(find_first_occurrence([1], 0), -1)

    def test_multiple_elements(self):
        self.assertEqual(find_first_occurrence([1, 2, 3], 2), 1)
        self.assertEqual(find_first_occurrence([1, 2, 3], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3], 0), -1)
        self.assertEqual(find_first_occurrence([3, 2, 1], 1), 2)
        self.assertEqual(find_first_occurrence([3, 2, 1], 2), 1)
        self.assertEqual(find_first_occurrence([3, 2, 1], 3), 0)

    def test_duplicate_elements(self):
        self.assertEqual(find_first_occurrence([1, 1, 2, 3], 1), 0)
        self.assertEqual(find_first_occurrence([1, 1, 2, 3], 2), 2)
        self.assertEqual(find_first_occurrence([1, 1, 2, 3], 3), 3)

    def test_edge_cases(self):
        self.assertEqual(find_first_occurrence([1], len(list(range(1000)))), -1)
        self.assertEqual(find_first_occurrence(list(range(1000)), 0), 0)
        self.assertEqual(find_first_occurrence(list(range(1000)), len(list(range(1000))) - 1), len(list(range(1000))) - 1)

    def test_error_cases(self):
        self.assertRaises(TypeError, find_first_occurrence, [1, 2, 3], "x")
        self.assertRaises(TypeError, find_first_occurrence, [], 1)
