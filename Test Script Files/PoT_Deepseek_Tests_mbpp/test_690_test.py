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
        self.assertEqual(mul_consecutive_nums([-1, -2, -3, -4]), [-2, -6, -12])

    def test_zero(self):
        self.assertEqual(mul_consecutive_nums([0, 1, 2, 3]), [0, 2, 6])

    def test_large_numbers(self):
        self.assertEqual(mul_consecutive_nums([100, 200, 300]), [20000, 60000])
