import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(re_order([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])
        self.assertEqual(re_order([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(re_order([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_conditions(self):
        self.assertEqual(re_order([]), [])
        self.assertEqual(re_order([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_complex_cases(self):
        self.assertEqual(re_order([0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0])
        self.assertEqual(re_order([1, 0, 2, 3, 0, 4]), [1, 2, 3, 4, 0, 0])
        self.assertEqual(re_order([0, 0, 1, 0, 2, 0]), [1, 2, 0, 0, 0, 0])
