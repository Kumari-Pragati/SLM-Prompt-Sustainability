import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3]), [[1, 1], [2, 2], [3, 3]])

    def test_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_all_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 1, 1]), [[1, 1, 1, 1]])

    def test_no_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 3]), [[1], [2], [3]])

    def test_negative_numbers(self):
        self.assertEqual(pack_consecutive_duplicates([-1, -1, -2, -2]), [[-1, -1], [-2, -2]])

    def test_mixed_numbers(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 3, 3, 1]), [[1], [2, 2], [3, 3], [1]])
