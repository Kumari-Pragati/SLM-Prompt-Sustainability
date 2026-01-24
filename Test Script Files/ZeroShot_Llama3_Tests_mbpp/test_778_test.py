import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_no_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 3, 4, 5]), [[1], [2], [3], [4], [5]])

    def test_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5]), [[1, 1], [2, 2, 2], [3, 3, 3, 3], [4], [5, 5]])

    def test_duplicates_at_start(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 3, 4, 5]), [[1, 1], [2], [3], [4], [5]])

    def test_duplicates_at_end(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 3, 4, 5, 5]), [[1], [2], [3], [4], [5, 5]])

    def test_duplicates_in_middle(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 3, 3, 4, 5, 5]), [[1], [2, 2], [3, 3], [4], [5, 5]])
