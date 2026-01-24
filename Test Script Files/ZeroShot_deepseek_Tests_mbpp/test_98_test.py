import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_multiply_num_with_positive_numbers(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4]), 2.4)

    def test_multiply_num_with_negative_numbers(self):
        self.assertAlmostEqual(multiply_num([-1, -2, -3, -4]), -0.9)

    def test_multiply_num_with_mixed_numbers(self):
        self.assertAlmostEqual(multiply_num([1, -2, 3, -4]), -1.2)

    def test_multiply_num_with_zero(self):
        self.assertEqual(multiply_num([0, 2, 3, 4]), 0)

    def test_multiply_num_with_single_number(self):
        self.assertEqual(multiply_num([5]), 5)

    def test_multiply_num_with_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])
