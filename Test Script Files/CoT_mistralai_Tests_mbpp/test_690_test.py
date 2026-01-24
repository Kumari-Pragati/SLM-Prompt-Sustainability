import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], mul_consecutive_nums([]))

    def test_single_element_list(self):
        self.assertListEqual([], mul_consecutive_nums([1]))

    def test_consecutive_numbers(self):
        self.assertListEqual([2, 4, 6], mul_consecutive_nums([1, 2, 3, 4]))

    def test_negative_numbers(self):
        self.assertListEqual([-2, 4, -6], mul_consecutive_nums([-1, -2, 3, 4]))

    def test_zero_in_middle(self):
        self.assertListEqual([0, 0, 0], mul_consecutive_nums([1, 0, 2, 0]))

    def test_floats(self):
        self.assertListEqual([2.0, 4.0, 6.0], mul_consecutive_nums([1.5, 2.0, 3.5]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            mul_consecutive_nums([1, 'a'])
