import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(nth_super_ugly_number(3, [2, 3, 5]), 12)
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 323)

    def test_edge_cases(self):
        self.assertEqual(nth_super_ugly_number(1, [2]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2]), 2)
        self.assertEqual(nth_super_ugly_number(3, [2]), 3)
        self.assertEqual(nth_super_ugly_number(4, [2]), 4)
        self.assertEqual(nth_super_ugly_number(1, [3]), 1)
        self.assertEqual(nth_super_ugly_number(2, [3]), 3)
        self.assertEqual(nth_super_ugly_number(3, [3]), 6)
        self.assertEqual(nth_super_ugly_number(4, [3]), 9)
        self.assertEqual(nth_super_ugly_number(1, [5]), 1)
        self.assertEqual(nth_super_ugly_number(2, [5]), 5)
        self.assertEqual(nth_super_ugly_number(3, [5]), 16)
        self.assertEqual(nth_super_ugly_number(4, [5]), 25)

    def test_complex(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 323)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7]), 2401)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7, 11]), 2677)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7, 11, 13]), 3089)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7, 11, 13, 17]), 3533)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7, 11, 13, 17, 19]), 3979)
