import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 6)

    def test_empty_array(self):
        A = []
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_single_element(self):
        A = [1]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_all_even_numbers(self):
        A = [2, 4, 6, 8]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 0)

    def test_all_odd_numbers(self):
        A = [1, 3, 5, 7]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 6)

    def test_mixed_numbers(self):
        A = [1, 2, 3, 4, 5, 6]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), 8)

    def test_large_numbers(self):
        A = [i for i in range(1, 10001) if i % 2 != 0]
        N = len(A)
        self.assertEqual(find_Odd_Pair(A, N), N * (N - 1) // 2)
