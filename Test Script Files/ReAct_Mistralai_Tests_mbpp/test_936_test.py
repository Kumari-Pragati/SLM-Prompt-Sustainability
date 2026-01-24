import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(re_arrange_tuples([], []), [])
        self.assertListEqual(re_arrange_tuples([], [1]), [(1, None)])
        self.assertListEqual(re_arrange_tuples([], [1, 2]), [(1, None), (2, None)])

    def test_single_element_lists(self):
        self.assertListEqual(re_arrange_tuples([(1, 2)], [1]), [(1, 2)])
        self.assertListEqual(re_arrange_tuples([(1, 2)], [2]), [(2, 1)])

    def test_ordering_match(self):
        self.assertListEqual(re_arrange_tuples([(1, 2), (3, 4)], [1, 2, 3, 4]), [(1, 2), (3, 4)])
        self.assertListEqual(re_arrange_tuples([(1, 2), (3, 4)], [2, 1, 3, 4]), [(2, 1), (3, 4)])
        self.assertListEqual(re_arrange_tuples([(1, 2), (3, 4)], [3, 1, 2, 4]), [(3, 1), (1, 2)])

    def test_ordering_mismatch(self):
        self.assertListEqual(re_arrange_tuples([(1, 2), (3, 4)], [1, 3, 2, 4]), [(1, 2), (3, 4)])
        self.assertListEqual(re_arrange_tuples([(1, 2), (3, 4)], [1, 3, 4, 2]), [(1, 2), (3, 4)])
        self.assertListEqual(re_arrange_tuples([(1, 2), (3, 4)], [3, 1, 4, 2]), [(3, 1), (1, 2)])

    def test_duplicate_keys(self):
        self.assertListEqual(re_arrange_tuples([(1, 2), (1, 3)], [1]), [(1, 2), (1, 3)])
        self.assertListEqual(re_arrange_tuples([(1, 2), (1, 3)], [2]), [(2, 1), (1, 3)])
        self.assertListEqual(re_arrange_tuples([(1, 2), (1, 3)], [3]), [(3, 1), (1, 2)])

    def test_missing_keys(self):
        self.assertListEqual(re_arrange_tuples([(1, 2), (3, 4)], [0]), [])
        self.assertListEqual(re_arrange_tuples([(1, 2), (3, 4)], [5]), [])
