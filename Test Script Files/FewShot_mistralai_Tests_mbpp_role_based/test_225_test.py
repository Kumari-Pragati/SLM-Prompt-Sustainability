import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):
    def test_find_min_single_element(self):
        self.assertEqual(find_Min([1], 0, 0), 1)

    def test_find_min_multiple_elements(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5]), 1)

    def test_find_min_sorted_array(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5]), 1)

    def test_find_min_reverse_sorted_array(self):
        self.assertEqual(find_Min([5, 4, 3, 2, 1]), 1)

    def test_find_min_duplicate_last_element(self):
        self.assertEqual(find_Min([1, 1, 2, 3, 4, 5]), 1)

    def test_find_min_duplicate_middle_element(self):
        self.assertEqual(find_Min([1, 2, 2, 3, 4, 5]), 2)

    def test_find_min_empty_array(self):
        with self.assertRaises(IndexError):
            find_Min([])

    def test_find_min_negative_array(self):
        self.assertEqual(find_Min([-1, -2, -3, -4, -5]), -1)
