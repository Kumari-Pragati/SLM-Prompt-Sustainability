import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), ([], []))

    def test_single_element_list(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_duplicate_elements(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3]), ([1, 2, 3], [2, 2, 1]))

    def test_no_duplicates(self):
        self.assertEqual(count_duplic([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]))

    def test_first_and_last_duplicate(self):
        self.assertEqual(count_duplic([1, 1]), ([1], [2]))

    def test_first_and_last_unique(self):
        self.assertEqual(count_duplic([1, 2]), ([1, 2], [1, 1]))

    def test_all_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 1]), ([1], [3]))

    def test_negative_numbers(self):
        self.assertEqual(count_duplic([-1, -1, 0, 1]), ([-1, 0, 1], [2, 1, 1]))

    def test_mixed_types(self):
        self.assertEqual(count_duplic([1, "a", 2, "a", 3]), ([1, "a", 2, "a"], [2, 1, 1]))
