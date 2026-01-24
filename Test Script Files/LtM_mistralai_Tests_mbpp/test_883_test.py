import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(div_of_nums([10, 20, 30], 2, 5), [10])
        self.assertListEqual(div_of_nums([4, 8, 12], 2, 4), [4, 8])

    def test_edge_and_boundary(self):
        self.assertListEqual(div_of_nums([], 2, 5), [])
        self.assertListEqual(div_of_nums([0], 2, 5), [])
        self.assertListEqual(div_of_nums([1], 2, 5), [])
        self.assertListEqual(div_of_nums([1, 2], 2, 2), [1, 2])
        self.assertListEqual(div_of_nums([1, 2], 3, 2), [])
        self.assertListEqual(div_of_nums([1, 2], 2, 1), [])

    def test_complex(self):
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 6, 3), [6])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 4, 3), [])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 2, 6), [])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 1, 1), [1])
