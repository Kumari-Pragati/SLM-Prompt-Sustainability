import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(re_order([1, 2, None, 4, 5]), [1, 2, 4, 5, None])
        self.assertListEqual(re_order(['a', None, 'b', 'c', None]), ['a', 'c', 'b', None, None])

    def test_edge_cases(self):
        self.assertListEqual(re_order([]), [])
        self.assertListEqual(re_order([None]), [])
        self.assertListEqual(re_order([None, None]), [None])
        self.assertListEqual(re_order([0, 0, 0]), [0, 0, 0])

    def test_boundary_cases(self):
        self.assertListEqual(re_order([1, None, 2, None, 3]), [1, 2, 3, None, None])
        self.assertListEqual(re_order([None, 1, None, 2, None]), [None, 1, 2, None, None])
        self.assertListEqual(re_order([1, 2, None, 3, None, 4]), [1, 2, 3, None, None, 4])
