import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 3)

    def test_empty_list(self):
        A = []
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_single_element(self):
        A = [1]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_all_even_numbers(self):
        A = [2, 4, 6, 8]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 6)

    def test_all_odd_numbers(self):
        A = [1, 3, 5, 7]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_mixed_numbers(self):
        A = [1, 2, 3, 4]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 2)

    def test_large_numbers(self):
        A = [i for i in range(1, 1001) if i % 2 == 0]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 499500)
