import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), [])

    def test_single_element_list(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_list_with_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), ([1, 2, 3, 4, 5], [2, 2, 2, 2, 1]))

    def test_list_with_duplicates_and_empty_list(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, []]), ([1, 2, 3, 4, 5], [2, 2, 2, 2, 1]))

    def test_list_with_duplicates_and_empty_list_and_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, [], [], 6, 6, 7, 7, 8, 8, 9, 9]), ([1, 2, 3, 4, 5, [], 6, 7, 8, 9], [2, 2, 2, 2, 1, 1, 2, 2, 2, 2]))
