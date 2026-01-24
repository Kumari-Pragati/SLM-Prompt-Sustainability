import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_negativenum([-1, 2, -3, 4]), -4)

    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_all_negative(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_all_positive(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_negativenum([-1, 2, -3, 4, 0]), -1)

    def test_large_numbers(self):
        self.assertEqual(sum_negativenum([-100, 200, -300, 400]), -1000)

    def test_float_numbers(self):
        self.assertEqual(sum_negativenum([-1.5, 2.5, -3.5]), -7.0)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            sum_negativenum(['-1', '2', '-3'])
