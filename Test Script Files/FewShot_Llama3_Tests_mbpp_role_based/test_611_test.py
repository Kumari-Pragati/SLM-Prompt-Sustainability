import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        self.assertEqual(max_of_nth(test_list, N), 9)

    def test_edge_case_empty_list(self):
        test_list = []
        N = 0
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)

    def test_edge_case_N_out_of_range(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertEqual(max_of_nth(test_list, N), 9)

    def test_edge_case_N_zero(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 0
        self.assertEqual(max_of_nth(test_list, N), max(sub[0] for sub in test_list))

    def test_edge_case_N_negative(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)
