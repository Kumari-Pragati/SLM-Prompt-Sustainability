import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(div_list([1, 2, 3], [2, 4, 6]), [0.5, 0.5, 0.5])

    def test_edge_case_zero(self):
        self.assertRaises(ZeroDivisionError, div_list, [1, 0], [2, 4])

    def test_edge_case_empty(self):
        self.assertRaises(TypeError, div_list, [1], [])

    def test_edge_case_different_lengths(self):
        self.assertRaises(IndexError, div_list, [1, 2], [3])

    def test_corner_case_negative(self):
        self.assertListEqual(div_list([-1, 2], [2, 4]), [-0.5, 0.5])
