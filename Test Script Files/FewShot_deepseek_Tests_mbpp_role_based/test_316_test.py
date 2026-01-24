import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):
    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 5, 6]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 5)

    def test_edge_case(self):
        A = [1, 2, 3, 4, 5, 5, 6]
        x = 10
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_boundary_case(self):
        A = []
        x = 10
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_invalid_input(self):
        A = [1, 2, 3, 4, 5, 5, 6]
        x = 'a'
        with self.assertRaises(TypeError):
            find_last_occurrence(A, x)
