import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 2, 5), [20, 40])

    def test_edge_case_with_single_number(self):
        self.assertEqual(div_of_nums([15], 3, 5), [15])

    def test_boundary_case_with_zero(self):
        self.assertEqual(div_of_nums([0], 2, 3), [0])

    def test_corner_case_with_negative_numbers(self):
        self.assertEqual(div_of_nums([-15, -10, -5], 5, 2), [-10, -5])

    def test_invalid_input_with_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            div_of_nums([10, 20, 30], 0, 2)

    def test_invalid_input_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            div_of_nums([10, 20.5, 30], 2, 5)
