import unittest
from649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_Range_list([], 1, 1), 0)

    def test_single_element(self):
        self.assertEqual(sum_Range_list([1], 1, 1), 1)
        self.assertEqual(sum_Range_list([1], 1, 2), 1)

    def test_multiple_elements(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 2, 4), 10)
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 3, 5), 15)

    def test_out_of_range(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 6, 6), 0)
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_Range_list([-1, -2, 3, 4, -5], 2, 4), -2)

    def test_large_numbers(self):
        self.assertEqual(sum_Range_list([1000000001, 1000000002, 1000000003], 2, 3), 3000000006)
