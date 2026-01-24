import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])
        self.assertEqual(max_sum_list([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])), [-1, -2, -3])

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sum_list([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum_list([[1]]), [[1]])
        self.assertEqual(max_sum_list([[-1]]), [[-1]])

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_sum_list([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(max_sum_list([[-1], [-2], [-3]]), [-1, -2, -3])
