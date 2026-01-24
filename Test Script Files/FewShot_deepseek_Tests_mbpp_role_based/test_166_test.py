import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):
    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 2)

    def test_edge_case_single_element(self):
        A = [1]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_boundary_case_empty_list(self):
        A = []
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_boundary_case_all_even_numbers(self):
        A = [2, 4, 6, 8]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 6)

    def test_boundary_case_all_odd_numbers(self):
        A = [1, 3, 5, 7]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_invalid_input_negative_numbers(self):
        A = [-1, -2, -3, -4]
        N = len(A)
        with self.assertRaises(Exception):
            find_even_Pair(A, N)

    def test_invalid_input_non_integer_numbers(self):
        A = [1.5, 2.5, 3.5, 4.5]
        N = len(A)
        with self.assertRaises(Exception):
            find_even_Pair(A, N)
