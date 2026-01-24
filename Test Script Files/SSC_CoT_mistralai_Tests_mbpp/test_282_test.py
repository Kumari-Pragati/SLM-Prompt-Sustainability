import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(sub_list([1, 2, 3], [2, 1, 0]), [3, 1, 3])
        self.assertListEqual(sub_list([0, -1, -2], [1, 0, 1]), [-1, -2, -3])

    def test_edge_cases(self):
        self.assertListEqual(sub_list([], []), [])
        self.assertListEqual(sub_list([0], []), [0])
        self.assertListEqual(sub_list([], [1]), [0])

    def test_boundary_cases(self):
        self.assertListEqual(sub_list([1, 2, 3], [1, 2, 3]), [0, 0, 0])
        self.assertListEqual(sub_list([-1, -2, -3], [-1, -2, -3]), [0, 0, 0])
        self.assertListEqual(sub_list([1, 2, 3], [-1, -2, -3]), [4, 5, 6])
        self.assertListEqual(sub_list([-1, -2, -3], [1, 2, 3]), [-4, -5, -6])
