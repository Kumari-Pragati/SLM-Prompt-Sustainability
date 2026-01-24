import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4]), [2, 3, 4])
        self.assertListEqual(add_consecutive_nums([5, 6, 7, 8]), [6, 7, 8])

    def test_edge_cases(self):
        self.assertListEqual(add_consecutive_nums([1]), [0])
        self.assertListEqual(add_consecutive_nums([1, 2]), [2])
        self.assertListEqual(add_consecutive_nums([1, 2, 3]), [2, 3])
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [2, 3, 4, 5])

    def test_boundary_conditions(self):
        self.assertListEqual(add_consecutive_nums([-1, 0, 1]), [-1, 0])
        self.assertListEqual(add_consecutive_nums([0, 1, 2, 3]), [1, 2, 3])
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6]), [2, 3, 4, 5, 6])

    def test_complex_cases(self):
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7]), [2, 3, 4, 5, 6, 7])
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8]), [2, 3, 4, 5, 6, 7, 8])
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]), [2, 3, 4, 5, 6, 7, 8, 9])
