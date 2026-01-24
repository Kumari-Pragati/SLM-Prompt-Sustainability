import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):

    def test_nth_super_ugly_number(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 24)
        self.assertEqual(nth_super_ugly_number(12, [2, 7, 3, 5]), 220)
        self.assertEqual(nth_super_ugly_number(16, [2, 7, 3, 5]), 4916)
        self.assertEqual(nth_super_ugly_number(20, [2, 3, 5, 9, 7]), 1106)
