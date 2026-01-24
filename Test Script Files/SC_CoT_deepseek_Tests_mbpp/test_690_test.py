import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4]), [2, 6])

    def test_edge_case_single_element(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(mul_consecutive_nums([-1, -2, -3, -4]), [2, 6])

    def test_corner_case_zero(self):
        self.assertEqual(mul_consecutive_nums([0, 1, 2, 3]), [0, 2])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            mul_consecutive_nums([1, '2', 3, 4])

    def test_invalid_input_empty_list(self):
        with self.assertRaises(IndexError):
            mul_consecutive_nums([1])
