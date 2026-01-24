import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 1), 0)

    def test_edge_cases(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 3), 2)

    def test_special_cases(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_first_occurrence([], 5), -1)
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 5], 0), -1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_first_occurrence(None, 5)
        with self.assertRaises(TypeError):
            find_first_occurrence([1, 2, 3, 4, 5], None)
