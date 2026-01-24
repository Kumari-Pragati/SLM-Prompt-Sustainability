import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):
    def test_typical_use_case(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 4)

    def test_edge_case_empty_list(self):
        A = []
        x = 5
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_edge_case_single_element_list(self):
        A = [5]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 0)

    def test_edge_case_list_with_duplicates(self):
        A = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 4)

    def test_edge_case_list_with_duplicates_and_duplicates(self):
        A = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]
        x = 5
        self.assertEqual(find_last_occurrence(A, x), 4)

    def test_invalid_input_non_list(self):
        A = "hello"
        x = 5
        with self.assertRaises(TypeError):
            find_last_occurrence(A, x)
