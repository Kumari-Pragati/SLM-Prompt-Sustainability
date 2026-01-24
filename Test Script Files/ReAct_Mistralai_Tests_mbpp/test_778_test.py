import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [[]])

    def test_single_element_list(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [ [1] ])

    def test_consecutive_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3, 3]), [ [1, 1], [2, 2], [3, 3, 3] ])

    def test_non_consecutive_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 1, 2, 3]), [ [1], [2], [1], [2], [3] ])

    def test_mixed_list(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 1, 2, 3, 4, 1, 2]), [ [1], [2], [1], [2], [3], [4], [1], [2] ])

    def test_negative_numbers(self):
        self.assertEqual(pack_consecutive_duplicates([-1, -1, 0, 0, -1]), [ [-1, -1], [0, 0], [-1] ])

    def test_empty_group(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 3, 4, 5, 1]), [ [1], [2], [3], [4], [5], [1] ])
