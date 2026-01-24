import unittest
from mbpp_798_code import _sum

class TestSum(unittest.TestCase):

    def test_sum_typical_case(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_sum_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_sum_single_element(self):
        self.assertEqual(_sum([10]), 10)

    def test_sum_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3, -4, -5]), -15)

    def test_sum_mixed_numbers(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 3)

    def test_sum_large_numbers(self):
        self.assertEqual(_sum(list(range(1, 10001))), 50005000)

    def test_sum_string_input(self):
        with self.assertRaises(TypeError):
            _sum(['1', '2', '3'])

    def test_sum_non_iterable_input(self):
        with self.assertRaises(TypeError):
            _sum(123)
