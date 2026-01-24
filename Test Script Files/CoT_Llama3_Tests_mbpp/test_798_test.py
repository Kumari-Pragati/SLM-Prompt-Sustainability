import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):

    def test_sum_of_positive_numbers(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_sum_of_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3, -4, -5]), -15)

    def test_sum_of_mixed_numbers(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 3)

    def test_sum_of_zero(self):
        self.assertEqual(_sum([0, 0, 0]), 0)

    def test_sum_of_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_sum_of_single_element(self):
        self.assertEqual(_sum([10]), 10)

    def test_sum_of_large_numbers(self):
        self.assertEqual(_sum([100, 200, 300, 400, 500]), 1300)

    def test_sum_of_float_numbers(self):
        self.assertEqual(_sum([1.0, 2.0, 3.0, 4.0, 5.0]), 15.0)

    def test_sum_of_string_input(self):
        with self.assertRaises(TypeError):
            _sum(['a', 'b', 'c'])

    def test_sum_of_mixed_types(self):
        with self.assertRaises(TypeError):
            _sum([1, 'a', 2, 3, 4])
