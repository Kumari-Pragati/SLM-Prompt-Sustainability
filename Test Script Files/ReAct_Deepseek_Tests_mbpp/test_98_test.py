import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4]), 2.5)

    def test_single_number(self):
        self.assertEqual(multiply_num([5]), 5)

    def test_zero_number(self):
        self.assertEqual(multiply_num([]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(multiply_num([-1, -2, -3]), -2.0)

    def test_zero_in_list(self):
        self.assertEqual(multiply_num([0, 1, 2]), 0)

    def test_large_numbers(self):
        self.assertAlmostEqual(multiply_num(list(range(1, 101))), 50.5)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])
