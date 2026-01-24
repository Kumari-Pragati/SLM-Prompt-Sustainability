import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), ([], []))

    def test_single_element_list(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_duplicate_element_list(self):
        self.assertEqual(count_duplic([1, 1, 2, 1, 2, 3]), ([1, 2, 2, 3], [2, 1, 1, 1]))

    def test_unique_elements_list(self):
        self.assertEqual(count_duplic([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]))

    def test_list_with_multiple_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3, 4, 4, 5]), ([1, 2, 3, 4], [2, 2, 2, 3, 2]))
