import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5, 6]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 3)

    def test_edge_case_single_element(self):
        A = [1]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_edge_case_two_elements(self):
        A = [1, 2]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 1)

    def test_edge_case_all_even(self):
        A = [2, 4, 6]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 1)

    def test_edge_case_all_odd(self):
        A = [1, 3, 5]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_corner_case_large_input(self):
        A = list(range(1, 10001))
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 49950000)

    def test_invalid_input_empty_list(self):
        A = []
        N = len(A)
        with self.assertRaises(Exception):
            find_even_Pair(A, N)

    def test_invalid_input_negative_elements(self):
        A = [-1, -2, -3, -4]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 3)

    def test_invalid_input_string_elements(self):
        A = ['1', '2', '3', '4']
        N = len(A)
        with self.assertRaises(Exception):
            find_even_Pair(A, N)
