import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 6, 12])

    def test_zero_in_middle(self):
        self.assertEqual(mul_consecutive_nums([1, 0, 3, 4]), [0, 0, 12])

    def test_single_element(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_empty_list(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_negative_numbers(self):
        self.assertEqual(mul_consecutive_nums([-1, -2, -3, -4]), [2, 6, 12, -24])
