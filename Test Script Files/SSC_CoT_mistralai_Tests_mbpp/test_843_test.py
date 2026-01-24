import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 32)
        self.assertEqual(nth_super_ugly_number(15, [2, 7, 13]), 364)

    def test_edge_cases(self):
        self.assertEqual(nth_super_ugly_number(1, [2]), 1)
        self.assertEqual(nth_super_ugly_number(2, [2]), 2)
        self.assertEqual(nth_super_ugly_number(3, [2]), 3)
        self.assertEqual(nth_super_ugly_number(4, [2]), 4)
        self.assertEqual(nth_super_ugly_number(5, [2]), 6)

        self.assertEqual(nth_super_ugly_number(10, [2]), 32)
        self.assertEqual(nth_super_ugly_number(10, [2, 3]), 32)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 32)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7]), 32)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7, 11]), 32)

        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7, 11, 13]), 32)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7, 11, 13, 17]), 32)
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5, 7, 11, 13, 17, 19]), 32)

        self.assertEqual(nth_super_ugly_number(100, [2, 3, 5, 7, 11, 13, 17, 19]), 2520)
        self.assertEqual(nth_super_ugly_number(100, [2, 3, 5, 7, 11, 13, 17, 19, 23]), 2520)
        self.assertEqual(nth_super_ugly_number(100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]), 2520)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, nth_super_ugly_number, 10, 1)
        self.assertRaises(TypeError, nth_super_ugly_number, 10, [1])
        self.assertRaises(TypeError, nth_super_ugly_number, 10, [2, 3, '5'])
        self.assertRaises(TypeError, nth_super_ugly_number, 10, [2, 3, 5, '7'])
