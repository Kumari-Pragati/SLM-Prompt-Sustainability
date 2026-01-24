import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5]), [
            [1, 1], [2, 2], [3, 3, 3], [4, 4, 4], [5]
        ])

    def test_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_consecutive_duplicates_with_gaps(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 1, 2, 3]), [[1], [2], [1], [2], [3]])

    def test_consecutive_duplicates_with_repetition(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 1, 2, 3]), [[1, 1], [2, 2], [1], [2], [3]])

    def test_non_consecutive_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 1, 3]), [[1], [2], [1], [3]])
