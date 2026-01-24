import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 32)
        self.assertEqual(nth_super_ugly_number(15, [2, 7, 3, 5]), 96)

    def test_single_prime(self):
        self.assertEqual(nth_super_ugly_number(10, [2]), 20)
        self.assertEqual(nth_super_ugly_number(10, [3]), 27)
        self.assertEqual(nth_super_ugly_number(10, [5]), 60)

    def test_edge_cases(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 3, 5]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2, 3, 5]), 2)
        self.assertEqual(nth_super_ugly_number(3, [2, 3, 5]), 6)
        self.assertEqual(nth_super_ugly_number(4, [2, 3, 5]), 12)
        self.assertEqual(nth_super_ugly_number(5, [2, 3, 5]), 24)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, nth_super_ugly_number, 10, 1)
        self.assertRaises(TypeError, nth_super_ugly_number, 10, [1])
