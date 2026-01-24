import unittest
from mbpp_859_code import combinations, chain, islice
from copy import deepcopy

from 859_code import sub_lists

class TestSubLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sub_lists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sub_lists([1]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(sub_lists([1, 2, 3]), [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def test_large_list(self):
        large_list = list(range(100))
        expected_sublists = list(chain.from_iterable(
            islice(combinations(large_list, i), None, None, i) for i in range(1, len(large_list) + 1)
        ))
        self.assertEqual(sub_lists(deepcopy(large_list)), expected_subsublists)

    def test_duplicate_elements(self):
        self.assertEqual(sub_lists([1, 1, 2]), [[1], [1], [2], [1, 1], [1, 2], [1, 1, 2]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sub_lists(123)
