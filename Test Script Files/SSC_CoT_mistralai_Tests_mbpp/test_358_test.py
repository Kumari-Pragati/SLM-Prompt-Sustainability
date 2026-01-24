import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertListEqual(moddiv_list([1, 2, 3, 4], [2, 3]), [1, 2, 0, 1])
        self.assertListEqual(moddiv_list([-1, 0, 1], [-2, 1, 3]), [-1, 0, 1])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(moddiv_list([0], [1]), [0])
        self.assertListEqual(moddiv_list([], [1]), [])
        self.assertListEqual(moddiv_list([1], []), [None])

    def test_negative_numbers(self):
        self.assertListEqual(moddiv_list([-1, -2], [1]), [-1, -2])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            moddiv_list('a', 'b')
        with self.assertRaises(TypeError):
            moddiv_list([1, 2], 'a')
