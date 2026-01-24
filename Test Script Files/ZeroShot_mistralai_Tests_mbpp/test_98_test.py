import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(multiply_num([]), 0)

    def test_single_number(self):
        self.assertEqual(multiply_num([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(multiply_num([1, 2, 3, 4, 5]), 1.4)

    def test_negative_numbers(self):
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5]), 1.4)

    def test_mixed_numbers(self):
        self.assertEqual(multiply_num([1, -2, 3, -4, 5]), 0.8)
