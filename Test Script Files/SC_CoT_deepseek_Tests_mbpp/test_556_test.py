import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 2)

    def test_edge_case(self):
        A = [1]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_boundary_case(self):
        A = []
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_odd_pair_exists(self):
        A = [1, 3, 5, 7]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 6)

    def test_all_even(self):
        A = [2, 4, 6, 8]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_negative_numbers(self):
        A = [-1, -3, -5, -7]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 6)

    def test_mixed_numbers(self):
        A = [1, -1, 2, -2]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Odd_Pair("1, 2, 3", 3)
