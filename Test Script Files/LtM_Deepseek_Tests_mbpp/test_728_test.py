import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edge_conditions(self):
        self.assertEqual(sum_list([], []), [])
        self.assertEqual(sum_list([1], [2]), [3])
        self.assertEqual(sum_list([0, 0, 0], [0, 0, 0]), [0, 0, 0])

    def test_boundary_conditions(self):
        self.assertEqual(sum_list([1000000000, 1000000000], [1000000000, 1000000000]), [2000000000, 2000000000])
        self.assertEqual(sum_list([-1000000000, -1000000000], [-1000000000, -1000000000]), [-2000000000, -2000000000])

    def test_complex_cases(self):
        self.assertEqual(sum_list([1, -2, 3], [4, -5, 6]), [5, -3, 9])
        self.assertEqual(sum_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), [7, 9, 11, 13, 15])
