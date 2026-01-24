import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 8)

    def test_edge_case_empty_list(self):
        test_list = []
        N = 0
        self.assertIsNone(max_of_nth(test_list, N))

    def test_boundary_case_single_element(self):
        test_list = [[1]]
        N = 0
        self.assertEqual(max_of_nth(test_list, N), 1)

    def test_corner_case_negative_numbers(self):
        test_list = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), -2)

    def test_corner_case_duplicate_max(self):
        test_list = [[1, 2, 3], [3, 2, 1], [1, 2, 3]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 3)

    def test_invalid_input_N_greater_than_length(self):
        test_list = [[1, 2, 3]]
        N = 4
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)
