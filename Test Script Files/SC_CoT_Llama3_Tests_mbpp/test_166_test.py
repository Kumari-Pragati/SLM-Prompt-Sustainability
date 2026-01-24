import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_typical_input(self):
        A = [1, 2, 3, 4, 5]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 2)

    def test_edge_case(self):
        A = [1, 2, 3, 4, 5, 6]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 3)

    def test_edge_case2(self):
        A = [2, 4, 6, 8, 10]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 5)

    def test_edge_case3(self):
        A = [1, 3, 5, 7, 9]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 0)

    def test_edge_case4(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        N = len(A)
        self.assertEqual(find_even_Pair(A, N), 5)

    def test_invalid_input1(self):
        A = [1, 2, 3, 4, 5]
        N = 'a'
        with self.assertRaises(TypeError):
            find_even_Pair(A, N)

    def test_invalid_input2(self):
        A = [1, 2, 3, 4, 5]
        N = -1
        with self.assertRaises(ValueError):
            find_even_Pair(A, N)
