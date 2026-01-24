import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), [])

    def test_single_element_list(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_duplicates_in_list(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3]), ([1, 2, 3], [2, 2, 3]))

    def test_no_duplicates_in_list(self):
        self.assertEqual(count_duplic([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]))

    def test_duplicates_at_end_of_list(self):
        self.assertEqual(count_duplic([1, 2, 3, 3, 3]), ([1, 2, 3], [1, 1, 3]))

    def test_duplicates_at_start_of_list(self):
        self.assertEqual(count_duplic([3, 3, 3, 2, 1]), ([3, 2, 1], [3, 1]))

    def test_duplicates_in_middle_of_list(self):
        self.assertEqual(count_duplic([1, 2, 2, 3, 3, 4]), ([1, 2, 3, 4], [1, 1, 2, 1]))
