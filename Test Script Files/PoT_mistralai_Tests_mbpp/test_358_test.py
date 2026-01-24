import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(moddiv_list([1, 2, 3, 4], [2, 3]), [1, 2, 0, 1])

    def test_edge_case_zero(self):
        self.assertListEqual(moddiv_list([0], [1]), [0])

    def test_edge_case_one(self):
        self.assertListEqual(moddiv_list([1], [0]), [1])

    def test_edge_case_empty(self):
        self.assertListEqual(moddiv_list([], [1]), [])

    def test_boundary_case_negative(self):
        self.assertListEqual(moddiv_list([-1, 0, 1], [-1, 2]), [-1, 1, 1])

    def test_corner_case_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, moddiv_list, [1], [0])
