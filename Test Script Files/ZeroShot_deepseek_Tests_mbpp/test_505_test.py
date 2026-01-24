import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_re_order(self):
        self.assertEqual(re_order([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(re_order([0]), [0])
        self.assertEqual(re_order([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(re_order([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(re_order([1, 0, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0])
