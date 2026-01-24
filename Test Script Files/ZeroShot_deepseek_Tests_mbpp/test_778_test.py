import unittest
from mbpp_778_code import groupby

def pack_consecutive_duplicates(list1):
    return [list(group) for key, group in groupby(list1)]

class TestPackConsecutiveDuplicates(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_no_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 3]), [[1], [2], [3]])

    def test_with_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3]), [[1, 1], [2, 2], [3]])

    def test_with_mixed_types(self):
        self.assertEqual(pack_consecutive_duplicates([1, 'a', 'a', 2, 2, 'b']), [[1], ['a', 'a'], [2, 2], ['b']])
