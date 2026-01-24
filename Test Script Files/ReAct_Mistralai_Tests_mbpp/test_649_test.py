import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            sum_Range_list([], 1, 2)

    def test_single_element(self):
        self.assertEqual(sum_Range_list([1], 1, 1), 1)

    def test_single_element_end(self):
        self.assertEqual(sum_Range_list([1], 1, 2), 1)

    def test_single_element_start(self):
        self.assertEqual(sum_Range_list([1], 2, 2), 1)

    def test_multiple_elements(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 2, 4), 10)

    def test_multiple_elements_end(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 1, 5), 15)

    def test_multiple_elements_start(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 3, 5), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_Range_list([-1, 0, 1], 1, 2), -1)

    def test_negative_start(self):
        self.assertEqual(sum_Range_list([-1, 0, 1], -1, 0), -1)

    def test_negative_end(self):
        self.assertEqual(sum_Range_list([-1, 0, 1], 0, 1), 1)

    def test_negative_numbers_start_end(self):
        self.assertEqual(sum_Range_list([-1, 0, 1], -1, 1), 0)

    def test_negative_numbers_start_end_empty(self):
        self.assertEqual(sum_Range_list([-1], -1, 0), -1)
