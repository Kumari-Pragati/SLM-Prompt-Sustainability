import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 8)

    def test_edge_case_N_greater_than_length(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 5
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)

    def test_empty_list(self):
        test_list = []
        N = 0
        with self.assertRaises(ValueError):
            max_of_nth(test_list, N)

    def test_negative_N(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)

    def test_N_equals_0(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 0
        self.assertEqual(max_of_nth(test_list, N), 1)
