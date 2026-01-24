import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(moddiv_list([1, 2, 3], [2, 3]), [1, 2, 0])
        self.assertListEqual(moddiv_list([4, 6, 8], [2, 3]), [0, 0, 2])
        self.assertListEqual(moddiv_list([10, 15, 20], [3, 4]), [1, 3, 0])

    def test_edge_cases(self):
        self.assertListEqual(moddiv_list([0], [1]), [0])
        self.assertListEqual(moddiv_list([1], []), [None])
        self.assertListEqual(moddiv_list([], [1]), [])
        self.assertListEqual(moddiv_list([-1, 0, 1], [2]), [-1, 0, 1])
        self.assertListEqual(moddiv_list([1, 2, 3], [-1, 0, 1]), [1, 2, 3])
