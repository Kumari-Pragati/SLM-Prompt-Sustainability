import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 2, 3, 4, 5, 6]
        x = 2
        self.assertEqual(find_last_occurrence(A, x), 2)

    def test_edge_case_single_element(self):
        A = [1]
        x = 1
        self.assertEqual(find_last_occurrence(A, x), 0)

    def test_edge_case_no_element(self):
        A = []
        x = 1
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_edge_case_all_same_elements(self):
        A = [1, 1, 1, 1, 1]
        x = 1
        self.assertEqual(find_last_occurrence(A, x), 4)

    def test_corner_case_first_element(self):
        A = [2, 3, 4, 5, 6]
        x = 2
        self.assertEqual(find_last_occurrence(A, x), 0)

    def test_corner_case_last_element(self):
        A = [1, 2, 3, 4, 5]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 4)

    def test_corner_case_not_exist(self):
        A = [1, 2, 3, 4, 5]
        x = 0
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_invalid_input_none(self):
        A = None
        x = 2
        with self.assertRaises(TypeError):
            find_last_occurrence(A, x)

    def test_invalid_input_empty_x(self):
        A = [1, 2, 3, 4, 5]
        x = None
        with self.assertRaises(TypeError):
            find_last_occurrence(A, x)
