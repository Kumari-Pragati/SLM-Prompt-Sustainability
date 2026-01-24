import unittest
from mbpp_778_code import islice, chain, repeat
from functools import reduce

from 778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [1])

    def test_consecutive_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3, 3]), [1, [1], [2, 2], [3, 3, 3]])

    def test_non_consecutive_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 1, 2, 3]), [1, [2], 1, [2, 3]])

    def test_mixed_types(self):
        self.assertEqual(pack_consecutive_duplicates([1, 'a', 1, 'a']), [1, ['a'], 1, ['a']])

    def test_invalid_input(self):
        self.assertRaises(TypeError, pack_consecutive_duplicates, (1, 2, 3))
        self.assertRaises(TypeError, pack_consecutive_duplicates, [1, 2, 3, 4].__iter__())

    def test_large_list(self):
        large_list = list(islice(chain(repeat(1, 1000), repeat(2, 1000)), 3000))
        expected = [1] * 1000 + [2] * 1000
        self.assertEqual(pack_consecutive_duplicates(large_list), expected)
