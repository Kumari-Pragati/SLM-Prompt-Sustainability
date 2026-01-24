import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(sum_num([1, 2, 3]), 2.0)

    def test_zero_numbers(self):
        self.assertEqual(sum_num([]), 0.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(sum_num([-1, -2, -3]), -1.5)

    def test_single_number(self):
        self.assertEqual(sum_num([4]), 4.0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            sum_num([])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            sum_num(None)
