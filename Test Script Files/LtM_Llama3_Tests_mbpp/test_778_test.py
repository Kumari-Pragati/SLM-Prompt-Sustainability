import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_single_element_input(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_consecutive_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]), [[1, 1], [2, 2, 2], [3, 3, 3]])

    def test_non_consecutive_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 3, 4, 5]), [[1], [2], [3], [4], [5]])

    def test_empty_list_with_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 1]), [[1, 1, 1]])

    def test_list_with_duplicates_and_non_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 3, 3, 4, 5, 5, 5]), [[1, 1], [2], [3, 3], [4], [5, 5, 5]])
