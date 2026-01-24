import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_duplic([]), [])

    def test_single_element_list(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_multiple_elements_list(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3, 4]), ([1, 2, 3, 4], [2, 2, 1]))

    def test_list_with_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 1, 2, 2, 3, 3, 3]), ([1, 2, 3], [3, 2, 1]))

    def test_list_with_no_duplicates(self):
        self.assertEqual(count_duplic([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]))

    def test_list_with_duplicates_at_end(self):
        self.assertEqual(count_duplic([1, 2, 3, 4, 4, 4]), ([1, 2, 3, 4], [1, 1, 1, 3]))
