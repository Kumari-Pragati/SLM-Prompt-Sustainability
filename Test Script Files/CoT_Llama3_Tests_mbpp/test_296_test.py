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
        self.assertEqual(get_Inv_Count([5, 2, 8, 1, 3], 5), 4)

    def test_duplicates(self):
        self.assertEqual(get_Inv_Count([1, 2, 2, 3, 3, 3], 6), 3)

    def test_negative_numbers(self):
        self.assertEqual(get_Inv_Count([-5, -2, 0, 1, 3], 5), 2)

    def test_large_array(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)
