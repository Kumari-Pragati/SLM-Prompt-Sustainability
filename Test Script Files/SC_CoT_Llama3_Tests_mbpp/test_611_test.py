import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_typical_input(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 9)

    def test_edge_case(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 6)

    def test_edge_case_empty_list(self):
        test_list = []
        N = 2
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)

    def test_edge_case_invalid_N(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 10
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)

    def test_edge_case_N_out_of_range(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)

    def test_typical_input_with_negative_numbers(self):
        test_list = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), -2)

    def test_typical_input_with_non_numeric_values(self):
        test_list = [[1, 2, 'a'], [4, 5, 'b'], [7, 8, 'c']]
        N = 2
        with self.assertRaises(TypeError):
            max_of_nth(test_list, N)
