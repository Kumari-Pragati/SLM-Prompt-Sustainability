import unittest
from mbpp_859_code import combinations, chain, islice
from copy import deepcopy

from 859_code import sub_lists

class TestSubLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sub_lists([]), [[]])

    def test_single_element_list(self):
        self.assertEqual(sub_lists([1]), [[1]])

    def test_two_element_list(self):
        self.assertEqual(sub_lists([1, 2]), [[1], [2], [1, 2]])

    def test_longer_list(self):
        test_list = [1, 2, 3, 4, 5]
        expected_sublists = list(chain.from_iterable(
            map(list, combinations(test_list, i)) for i in range(1, len(test_list) + 1)
        ))
        self.assertEqual(sub_lists(test_list), expected_sublists)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            sub_lists([1, 2, 3])[-1]

    def test_list_with_duplicates(self):
        test_list = [1, 1, 2, 2, 3]
        expected_sublists = list(chain.from_iterable(
            map(list, combinations(test_list, i)) for i in range(1, len(test_list) + 1)
        ))
        self.assertEqual(sub_lists(test_list), expected_sublists)

    def test_large_list(self):
        test_list = list(range(1000))
        expected_sublists = list(chain.from_iterable(
            map(list, combinations(test_list, i)) for i in range(1, len(test_list) + 1)
        ))
        self.assertEqual(sub_lists(test_list), expected_sublists)

    def test_list_with_large_sublists(self):
        test_list = list(range(100000))
        expected_sublists = list(chain.from_iterable(
            map(list, combinations(test_list, i)) for i in range(1, len(test_list) + 1)
        ))
        self.assertEqual(sub_lists(test_list), expected_sublists)
