import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_Range_list([], 0, 0), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_Range_list([1], 0, 0), 1)

    def test_single_element_list_out_of_range(self):
        self.assertEqual(sum_Range_list([1], 1, 1), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(sum_Range_list([1, 2, 3], 0, 2), 6)

    def test_multiple_elements_list_out_of_range(self):
        self.assertEqual(sum_Range_list([1, 2, 3], 1, 2), 3)

    def test_negative_range(self):
        self.assertEqual(sum_Range_list([-1, 0, 1], -1, 1), 0)

    def test_positive_range(self):
        self.assertEqual(sum_Range_list([1, 2, 3], 1, 3), 6)

    def test_zero_range(self):
        self.assertEqual(sum_Range_list([1, 2, 3], 0, 0), 0)

    def test_invalid_range(self):
        with self.assertRaises(IndexError):
            sum_Range_list([1, 2, 3], 3, 2)
