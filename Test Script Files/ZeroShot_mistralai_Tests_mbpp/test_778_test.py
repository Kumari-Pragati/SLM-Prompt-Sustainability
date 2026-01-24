import unittest
from mbpp_778_code import groupby

def pack_consecutive_duplicates(list1):
    return [list(group) for key, group in groupby(list1)]

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [[]])

    def test_single_element_list(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [ [1] ])

    def test_simple_list(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 1, 2, 2, 3, 2, 2, 2, 1]), [ [1, 1], [2], [1], [2, 2, 2], [3], [2, 2, 2], [1] ])

    def test_list_with_duplicates_at_start_and_end(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 1, 1]), [ [1, 1], [2, 2, 2, 2], [3], [2, 2, 2], [1, 1] ])

    def test_list_with_duplicates_in_middle(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 2, 3, 4, 2, 2, 2, 5, 6, 2, 2]), [ [1], [2, 2, 2], [3], [4], [2, 2, 2], [5], [6], [2, 2] ])
