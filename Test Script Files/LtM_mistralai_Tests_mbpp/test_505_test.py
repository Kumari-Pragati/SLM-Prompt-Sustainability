import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(re_order([1, 2, 3, None, 5, 0]), [1, 2, 3, None, 5, 0])
        self.assertListEqual(re_order([0, 1, 2, None, 5]), [0, 1, 2, None, 5])
        self.assertListEqual(re_order([None, 0, 1, 2]), [None, 0, 1, 2])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(re_order([]), [])
        self.assertListEqual(re_order([None]), [None])
        self.assertListEqual(re_order([0] * 100), [0] * 100)
        self.assertListEqual(re_order([None] * 100), [None] * 100)

    def test_complex_inputs(self):
        self.assertListEqual(re_order([None, 0, None, 1, None, 2]), [None, 0, None, 1, None, 2])
        self.assertListEqual(re_order([0, None, 1, None, 2]), [0, None, 1, None, 2])
        self.assertListEqual(re_order([None] + [0] * 100), [None] + [0] * 100)
