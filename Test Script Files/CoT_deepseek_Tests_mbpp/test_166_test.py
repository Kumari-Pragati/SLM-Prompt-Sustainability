import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 3)

    def test_all_even_case(self):
        A = [2, 4, 6, 8]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 6)

    def test_all_odd_case(self):
        A = [1, 3, 5, 7]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_single_element_case(self):
        A = [1]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_empty_array_case(self):
        A = []
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_negative_numbers_case(self):
        A = [-1, -2, -3, -4]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 6)

    def test_mixed_numbers_case(self):
        A = [-1, 2, -3, 4]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 2)

    def test_large_numbers_case(self):
        A = [10**6, 2*10**6, 3*10**6, 4*10**6]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 6)

    def test_large_input_case(self):
        A = list(range(1, 10**4))
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 4995000)
