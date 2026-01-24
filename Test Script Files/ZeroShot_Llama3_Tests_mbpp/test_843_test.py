import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_nth_super_ugly_number(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 7, 13, 19]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2, 7, 13, 19]), 2)
        self.assertEqual(nth_super_ugly_number(3, [2, 7, 13, 19]), 4)
        self.assertEqual(nth_super_ugly_number(4, [2, 7, 13, 19]), 7)
        self.assertEqual(nth_super_ugly_number(5, [2, 7, 13, 19]), 14)
        self.assertEqual(nth_super_ugly_number(6, [2, 7, 13, 19]), 22)
        self.assertEqual(nth_super_ugly_number(7, [2, 7, 13, 19]), 28)
        self.assertEqual(nth_super_ugly_number(8, [2, 7, 13, 19]), 35)
        self.assertEqual(nth_super_ugly_number(9, [2, 7, 13, 19]), 52)
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 65)

    def test_nth_super_ugly_number_edge_cases(self):
        self.assertRaises(ValueError, nth_super_ugly_number, 0, [2, 7, 13, 19])
        self.assertRaises(ValueError, nth_super_ugly_number, 1, [])
