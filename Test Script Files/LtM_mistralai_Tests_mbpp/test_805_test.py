import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_sum_list([[1], [3], [2]]), [3])
        self.assertEqual(max_sum_list([[-1], [-3], [-2]]), [-1])
        self.assertEqual(max_sum_list([[0], [0], [0]]), [0])

    def test_edge_cases(self):
        self.assertEqual(max_sum_list([]), [])
        self.assertEqual(max_sum_list([[1], [2], [3], [4], [5]]), [[1], [2], [3], [4], [5]])
        self.assertEqual(max_sum_list([[-1], [-2], [-3], [-4], [-5]]), [[-1], [-2], [-3], [-4], [-5]])
        self.assertEqual(max_sum_list([[1000000000], [1], [2], [3], [4], [5]]), [[1000000000], [1], [2], [3], [4], [5]])
        self.assertEqual(max_sum_list([[-1000000000], [-1], [-2], [-3], [-4], [-5]]), [[-1000000000], [-1], [-2], [-3], [-4], [-5]])

    def test_complex_cases(self):
        self.assertEqual(max_sum_list([[1, 2], [3, 4], [5, 6]]), [[3, 4], [5, 6]])
        self.assertEqual(max_sum_list([[-1, -2], [-3, -4], [-5, -6]]), [[-1, -2], [-3, -4], [-5, -6]])
        self.assertEqual(max_sum_list([[1, -2], [3, 4], [5, -6]]), [[3, 4], [5, -6]])
        self.assertEqual(max_sum_list([[-1, 2], [-3, 4], [-5, 6]]), [[-1, 2], [-3, 4], [-5, 6]])
