import unittest
from mbpp_733_code import find_first_occurrence

class TestFindFirstOccurrence(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 4)

    def test_edge_case_first_element(self):
        A = [5, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 0)

    def test_edge_case_last_element(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 5]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 8)

    def test_edge_case_single_element(self):
        A = [5]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), 0)

    def test_edge_case_not_found(self):
        A = [1, 2, 3, 4, 6, 7, 8, 9]
        x = 5
        self.assertEqual(find_first_occurrence(A, x), -1)

    def test_invalid_input_empty_list(self):
        A = []
        x = 5
        self.assertEqual(find_first_occurrence(A, x), -1)

    def test_invalid_input_non_integer_elements(self):
        A = [1, 2, '3', 4, 5, 6, 7, 8, 9]
        x = 5
        with self.assertRaises(TypeError):
            find_first_occurrence(A, x)
