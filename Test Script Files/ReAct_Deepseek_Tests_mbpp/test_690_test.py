import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2, 6, 12, 20])

    def test_single_element(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_empty_list(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_negative_numbers(self):
        self.assertEqual(mul_consecutive_nums([-1, -2, -3, -4, -5]), [-2, -6, -12, -20])

    def test_zero_and_positive(self):
        self.assertEqual(mul_consecutive_nums([0, 1, 2, 3, 4]), [0, 2, 6, 12])

    def test_large_numbers(self):
        self.assertEqual(mul_consecutive_nums([1000000, 2000000, 3000000]), [2000000, 6000000])

    def test_float_numbers(self):
        self.assertEqual(mul_consecutive_nums([1.5, 2.5, 3.5]), [4.0])

    def test_mixed_numbers(self):
        self.assertEqual(mul_consecutive_nums([1, 2.5, 3, 4]), [5.0, 10.0])
