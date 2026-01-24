import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_num([1, 2, 3]), 2.0)

    def test_empty_list(self):
        self.assertRaises(ZeroDivisionError, sum_num, [])

    def test_single_element(self):
        self.assertEqual(sum_num([5]), 5)

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, sum_num, [0])

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sum_num([1, 2, 'a'])

    def test_negative_numbers(self):
        self.assertEqual(sum_num([-1, -2, -3]), -2.0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_num([1, -2, 3, -4]), -0.5)
