import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(sub_list([1, 2, 3], [0, 1, 2]), [1, 0, 0])
        self.assertListEqual(sub_list([-1, -2, -3], [0, 1, 2]), [-1, -3, -5])

    def test_edge_cases(self):
        self.assertListEqual(sub_list([], []), [])
        self.assertListEqual(sub_list([1], []), [1])
        self.assertListEqual(sub_list([], [1]), [])
        self.assertListEqual(sub_list([1], [1]), [0])

    def test_complex(self):
        self.assertListEqual(sub_list([1, 2, 3], [3, 2, 1]), [-2, 0, -2])
        self.assertListEqual(sub_list([-1, -2, -3], [-3, -2, -1]), [0, 1, 2])
        self.assertListEqual(sub_list([1, 2, 3], [-3, -2, -1]), [4, 5, 4])
        self.assertListEqual(sub_list([-1, -2, -3], [3, 2, 1]), [-4, -4, -4])
