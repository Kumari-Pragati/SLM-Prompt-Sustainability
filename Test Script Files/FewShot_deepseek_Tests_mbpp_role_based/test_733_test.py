import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):
    def test_typical_use_case(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 4)

    def test_edge_condition(self):
        A = [1]
        x = 1
        self.assertEqual(find_first_occurrence(A, x), 0)

    def test_boundary_condition(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 10
        self.assertEqual(find_first_occurrence(A, x), -1)

    def test_invalid_input(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 'a'
        with self.assertRaises(TypeError):
            find_first_occurrence(A, x)
