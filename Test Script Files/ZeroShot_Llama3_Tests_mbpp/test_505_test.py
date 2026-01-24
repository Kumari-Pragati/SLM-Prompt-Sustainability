import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_re_order(self):
        self.assertEqual(re_order([1, 0, 1, 0, 1]), [1, 1, 1, 0, 0])
        self.assertEqual(re_order([0, 1, 0, 1, 0]), [1, 0, 1, 0, 0])
        self.assertEqual(re_order([1, 1, 1, 0, 0]), [1, 1, 1, 0, 0])
        self.assertEqual(re_order([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(re_order([1, 1, 0, 0, 0]), [1, 1, 0, 0, 0])
        self.assertEqual(re_order([0, 1, 1, 0, 0]), [1, 1, 0, 0, 0])

    def test_re_order_empty(self):
        self.assertEqual(re_order([]), [])

    def test_re_order_single(self):
        self.assertEqual(re_order([1]), [1])

    def test_re_order_zero(self):
        self.assertEqual(re_order([0]), [0])
