import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_Range_list([], 1, 1), 0)

    def test_single_element(self):
        self.assertEqual(sum_Range_list([1], 1, 1), 1)

    def test_simple_range(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 2, 4), 10)

    def test_negative_range(self):
        self.assertEqual(sum_Range_list([-1, -2, -3, -4, -5], 3, 1), -10)

    def test_out_of_range_start(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 6, 6), 0)

    def test_out_of_range_end(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 1, 7), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_Range_list([-1, -2, -3, -4, -5], 2, 4), -10)

    def test_m_greater_than_n(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 6, 1), 0)

    def test_m_equal_to_n(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 5, 5), 15)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            sum_Range_list('invalid', 1, 2)

    def test_invalid_input_m(self):
        with self.assertRaises(TypeError):
            sum_Range_list([1, 2, 3], 'invalid', 2)

    def test_invalid_input_n(self):
        with self.assertRaises(TypeError):
            sum_Range_list([1, 2, 3], 1, 'invalid')
