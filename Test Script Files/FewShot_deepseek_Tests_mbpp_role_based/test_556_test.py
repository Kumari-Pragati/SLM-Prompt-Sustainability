import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):
    def test_typical_use_case(self):
        A = [1, 2, 3, 4, 5]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 6)

    def test_edge_case_with_single_element(self):
        A = [1]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_boundary_case_with_empty_list(self):
        A = []
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_odd_pair_in_list(self):
        A = [1, 3, 5, 7]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 6)

    def test_no_odd_pair_in_list(self):
        A = [2, 4, 6, 8]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_negative_numbers(self):
        A = [-1, -3, -5, -7]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 6)

    def test_mixed_numbers(self):
        A = [1, -1, 2, -2, 3, -3]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 6)
