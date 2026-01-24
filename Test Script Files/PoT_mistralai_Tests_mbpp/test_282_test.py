import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(sub_list([1, 2, 3], [2, 1, 0]), [3, 1, 3])
        self.assertListEqual(sub_list([-1, -2, -3], [-2, -1, 0]), [1, -1, -3])
        self.assertListEqual(sub_list([0, 0, 0], [1, 1, 1]), [-1, -1, -1])

    def test_edge_case(self):
        self.assertListEqual(sub_list([], []), [])
        self.assertListEqual(sub_list([1], []), [1])
        self.assertListEqual(sub_list([], [1]), [])

    def test_boundary_case(self):
        self.assertListEqual(sub_list([-1], [0]), [-1])
        self.assertListEqual(sub_list([0], [-1]), [0])
        self.assertListEqual(sub_list([0], [0]), [0])
