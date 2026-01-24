import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):
    def test_typical_input(self):
        A = [1, 2, 3, 4, 5]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 1)

    def test_edge_case_N_zero(self):
        A = []
        N = 0
        with self.assertRaises(IndexError):
            find_Odd_Pair(A, N)

    def test_edge_case_N_one(self):
        A = [1]
        N = 1
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_edge_case_N_two(self):
        A = [1, 2]
        N = 2
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_edge_case_N_three(self):
        A = [1, 2, 3]
        N = 3
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_edge_case_A_empty(self):
        A = []
        N = 5
        with self.assertRaises(IndexError):
            find_Odd_Pair(A, N)

    def test_edge_case_A_single_element(self):
        A = [1]
        N = 1
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_edge_case_A_two_elements(self):
        A = [1, 2]
        N = 2
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_edge_case_A_three_elements(self):
        A = [1, 2, 3]
        N = 3
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_edge_case_A_four_elements(self):
        A = [1, 2, 3, 4]
        N = 4
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_edge_case_A_five_elements(self):
        A = [1, 2, 3, 4, 5]
        N = 5
        self.assertEqual(find_Odd_Pair(A, N), 1)

    def test_edge_case_A_six_elements(self):
        A = [1, 2, 3, 4, 5, 6]
        N = 6
        self.assertEqual(find_Odd_Pair(A, N), 2)

    def test_edge_case_A_seven_elements(self):
        A = [1, 2, 3, 4, 5, 6, 7]
        N = 7
        self.assertEqual(find_Odd_Pair(A, N), 3)

    def test_edge_case_A_eight_elements(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        N = 8
        self.assertEqual(find_Odd_Pair(A, N), 3)

    def test_edge_case_A_nine_elements(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        N = 9
        self.assertEqual(find_Odd_Pair(A, N), 4)

    def test_edge_case_A_ten_elements(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        N = 10
        self.assertEqual(find_Odd_Pair(A, N), 4)
