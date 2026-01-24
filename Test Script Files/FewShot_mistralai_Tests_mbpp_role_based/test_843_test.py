import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 3, 5]), 24)
        self.assertEqual(nth_super_ugly_number(15, [2, 7, 13]), 181)

    def test_single_prime(self):
        self.assertEqual(nth_super_ugly_number(10, [2]), 20)
        self.assertEqual(nth_super_ugly_number(10, [3]), 27)
        self.assertEqual(nth_super_ugly_number(10, [5]), 60)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(10, [])

    def test_single_input(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(1, [2])

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            nth_super_ugly_number(-10, [2, 3, 5])
