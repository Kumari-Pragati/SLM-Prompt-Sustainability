import unittest
from mbpp_333_code import Sort

class TestSort(unittest.TestCase):

    def test_sort_with_valid_input(self):
        self.assertEqual(Sort([(1, 2), (3, 4), (5, 1)]), [(5, 1), (1, 2), (3, 4)])
        self.assertEqual(Sort([(1, 2), (3, 2), (5, 1)]), [(5, 1), (1, 2), (3, 2)])

    def test_sort_with_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_sort_with_same_second_element(self):
        self.assertEqual(Sort([(1, 2), (3, 2), (5, 2)]), [(5, 2), (1, 2), (3, 2)])

    def test_sort_with_negative_numbers(self):
        self.assertEqual(Sort([(1, -2), (3, -4), (5, -1)]), [(5, -1), (1, -2), (3, -4)])
