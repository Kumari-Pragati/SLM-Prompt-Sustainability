import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):
    def test_sum_range_list_positive_numbers(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 4
        self.assertEqual(sum_range_list(list1, m, n), 10)

    def test_sum_range_list_negative_numbers(self):
        list1 = [-1, -2, -3, -4, -5]
        m = 2
        n = 4
        self.assertEqual(sum_range_list(list1, m, n), -6)

    def test_sum_range_list_zero(self):
        list1 = [0, 0, 0, 0, 0]
        m = 1
        n = 5
        self.assertEqual(sum_range_list(list1, m, n), 0)

    def test_sum_range_list_out_of_range(self):
        list1 = [1, 2, 3, 4, 5]
        m = 5
        n = 5
        self.assertEqual(sum_range_list(list1, m, n), 5)

    def test_sum_range_list_invalid_input_type(self):
        list1 = [1, 2, 3, 4, 5]
        m = 'a'
        n = 4
        with self.assertRaises(TypeError):
            sum_range_list(list1, m, n)
