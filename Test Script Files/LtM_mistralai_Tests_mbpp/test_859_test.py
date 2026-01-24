import unittest
from mbpp_859_code import chain, combinations

class TestSubLists(unittest.TestCase):

    def test_simple_list(self):
        self.assertListEqual(sub_lists([1, 2, 3]), [
            [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
        ])

    def test_empty_list(self):
        self.assertListEqual(sub_lists([]), [[]])

    def test_single_element_list(self):
        self.assertListEqual(sub_lists([1]), [[1]])

    def test_negative_index(self):
        self.assertListEqual(sub_lists([1, 2, 3]), [])

    def test_large_list(self):
        large_list = list(range(100))
        self.assertListEqual(sub_lists(large_list), list(chain.from_iterable(
            [combinations(large_list, i) for i in range(len(large_list) + 1)]
        )))

    def test_duplicate_elements(self):
        self.assertListEqual(sub_lists([1, 1, 2, 3]), [
            [], [1], [1, 1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 1, 2], [1, 1, 3], [1, 2, 3], [1, 1, 2, 3]
        ])
