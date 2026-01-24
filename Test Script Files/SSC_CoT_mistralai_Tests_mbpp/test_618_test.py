import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_normal(self):
        self.assertListEqual(div_list([1, 2, 3], [1, 2, 3]), [1.0, 1.5, 1.5])
        self.assertListEqual(div_list([4, 4, 4], [2, 2, 2]), [2.0, 2.0, 2.0])

    def test_edge_cases(self):
        self.assertRaises(TypeError, div_list, [1, 2], 0)
        self.assertRaises(TypeError, div_list, [1, 2], "string")
        self.assertListEqual(div_list([0], [1]), [0.0])
        self.assertListEqual(div_list([1], [0]), [None])

    def test_boundary_cases(self):
        self.assertListEqual(div_list([-1, 1], [2]), [-0.5, 0.5])
        self.assertListEqual(div_list([1, -1], [2]), [0.5, -0.5])
        self.assertListEqual(div_list([1, 1], [0, 2]), [None, 0.5])
        self.assertListEqual(div_list([0, 1], [0, 2]), [None, 0.5])
