import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(multiply_num([]), 0)

    def test_single_number(self):
        self.assertEqual(multiply_num([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(multiply_num([1, 2, 3, 4, 5]), 1.6)

    def test_negative_numbers(self):
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5]), -1.6)

    def test_zero_in_list(self):
        self.assertEqual(multiply_num([0, 1, 2, 3, 4]), 1.2)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(multiply_num([1.1, 2.2, 3.3, 4.4, 5.5]), 11.56, delta=0.01)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply_num("not a number")
