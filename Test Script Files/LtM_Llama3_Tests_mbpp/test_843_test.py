import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 7, 13, 21]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2, 7, 13, 21]), 2)
        self.assertEqual(nth_super_ugly_number(3, [2, 7, 13, 21]), 4)
        self.assertEqual(nth_super_ugly_number(4, [2, 7, 13, 21]), 6)
        self.assertEqual(nth_super_ugly_number(5, [2, 7, 13, 21]), 8)

    def test_edge(self):
        self.assertEqual(nth_super_ugly_number(1, []), 1)
        self.assertEqual(nth_super_ugly_number(1, [1]), 1)
        self.assertEqual(nth_super_ugly_number(1, [1, 1]), 1)
        self.assertEqual(nth_super_ugly_number(1, [1, 2]), 1)
        self.assertEqual(nth_super_ugly_number(1, [1, 2, 3]), 1)

    def test_complex(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 21]), 32)
        self.assertEqual(nth_super_ugly_number(10, [1, 2, 3, 4, 5]), 12)
        self.assertEqual(nth_super_ugly_number(10, [1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(nth_super_ugly_number(10, [1, 2, 3, 4, 5, 6, 7]), 12)
