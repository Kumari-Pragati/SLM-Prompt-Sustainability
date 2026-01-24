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

    def test_zero(self):
        self.assertEqual(mul_consecutive_nums([0, 1, 2, 3, 4]), [0, 2, 6, 12])

    def test_large_numbers(self):
        self.assertEqual(mul_consecutive_nums(list(range(1, 100))), list(range(1, 100))[1:]*list(range(1, 100))[:-1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            mul_consecutive_nums('1, 2, 3, 4, 5')

        with self.assertRaises(TypeError):
            mul_consecutive_nums(123)

        with self.assertRaises(TypeError):
            mul_consecutive_nums(None)
