import unittest
from mbpp_819_code import count_duplic

class TestCountDuplic(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_duplic([]), ([], []))

    def test_single_element(self):
        self.assertEqual(count_duplic([1]), ([1], [1]))

    def test_no_duplicates(self):
        self.assertEqual(count_duplic([1, 2, 3, 4]), ([1, 2, 3, 4], [1, 1, 1, 1]))

    def test_with_duplicates(self):
        self.assertEqual(count_duplic([1, 1, 2, 2, 3, 3]), ([1, 2, 3], [2, 2, 2]))

    def test_with_duplicates_at_end(self):
        self.assertEqual(count_duplic([1, 2, 2, 3, 3, 3]), ([1, 2, 3], [1, 2, 3]))
