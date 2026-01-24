import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_nth_super_ugly_number(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 238)
        self.assertEqual(nth_super_ugly_number(1, [2, 3, 5]), 1)
        self.assertEqual(nth_super_ugly_number(15, [3, 5, 7]), 500)
        self.assertEqual(nth_super_ugly_number(1000, [2, 3, 5]), 512000)
