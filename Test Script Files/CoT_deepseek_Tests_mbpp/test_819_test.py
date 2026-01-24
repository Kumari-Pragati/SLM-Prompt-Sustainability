import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), ([], []))

    def test_single_element(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_no_duplicates(self):
        self.assertEqual(count_duplic([1, 2, 3, 4]), ([1, 2, 3, 4], [1, 1, 1, 1]))

    def test_multiple_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3]), ([1, 2, 3], [2, 2, 2]))

    def test_duplicates_at_ends(self):
        self.assertEqual(count_duplic([1, 2, 2, 3]), ([1, 2, 3], [1, 2, 1]))

    def test_duplicates_in_middle(self):
        self.assertEqual(count_duplic([1, 2, 2, 3, 3, 4]), ([1, 2, 3, 4], [1, 2, 2, 1]))

    def test_large_list(self):
        self.assertEqual(count_duplic(list(range(1, 1001))), ([1], [1000]))
