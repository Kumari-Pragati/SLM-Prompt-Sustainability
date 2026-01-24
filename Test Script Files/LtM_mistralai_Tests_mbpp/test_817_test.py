import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(div_of_nums([12, 18, 24], 3, 4), [12, 18])
        self.assertListEqual(div_of_nums([2, 4, 6], 2, 3), [2, 4])

    def test_edge_and_boundary(self):
        self.assertListEqual(div_of_nums([0], 2, 3), [])
        self.assertListEqual(div_of_nums([1], 2, 3), [])
        self.assertListEqual(div_of_nums([1, 2, 3], 1, 2), [1, 2, 3])
        self.assertListEqual(div_of_nums([1, 2, 3], 0, 2), [])
        self.assertListEqual(div_of_nums([1, 2, 3], 2, 0), [])

    def test_complex(self):
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 6, 7), [1, 3, 5])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 7, 6), [1, 2, 3, 4, 5])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 6, 5), [1, 3, 5])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 5, 6), [1, 2, 3, 4])
