import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3, 3]), [[1, 1], [2, 2], [3, 3, 3]])

    def test_single_element_list(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_consecutive_duplicates_at_start(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 2, 3]), [[1, 1], [2, 2, 2], [3]])

    def test_consecutive_duplicates_at_end(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 2, 3, 3]), [[1], [2, 2, 2], [3, 3]])

    def test_consecutive_duplicates_in_middle(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 2, 3, 3, 4, 4, 4]), [[1], [2, 2, 2], [3, 3], [4, 4, 4]])
