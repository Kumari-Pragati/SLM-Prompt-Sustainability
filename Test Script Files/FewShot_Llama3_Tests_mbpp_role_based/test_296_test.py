import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(get_Inv_Count([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_Inv_Count([1], 1), 0)

    def test_sorted_array(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5], 5), 0)

    def test_unsorted_array(self):
        self.assertEqual(get_Inv_Count([5, 1, 4, 2, 3], 5), 4)

    def test_array_with_duplicates(self):
        self.assertEqual(get_Inv_Count([1, 2, 2, 3, 3, 4, 5], 7), 6)

    def test_array_with_negative_numbers(self):
        self.assertEqual(get_Inv_Count([-1, -2, -3, -4, -5], 5), 0)

    def test_array_with_negative_and_positive_numbers(self):
        self.assertEqual(get_Inv_Count([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], 10), 0)
