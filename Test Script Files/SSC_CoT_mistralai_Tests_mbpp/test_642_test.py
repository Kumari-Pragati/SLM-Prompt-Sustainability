import unittest
from mbpp_642_code import frozenset
from six.moves import range
from collections import deque

from 642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_normal_input(self):
        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [3, 2, 1], [1, 2, 3]]),
            frozenset([frozenset([1, 2, 3])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [3, 2, 1], [1, 2, 3], [1, 2, 4]]),
            frozenset([frozenset([1, 2, 3]), frozenset([1, 2, 4])])
        )

    def test_edge_and_boundary_conditions(self):
        self.assertCountEqual(
            remove_similar_row([[1], [1]]),
            frozenset([frozenset([1])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2], [2, 1]]),
            frozenset([frozenset([1, 2])])
        )

        self.assertCountEqual(
            remove_similar_row([[1], [2], [3]]),
            frozenset([frozenset([1]), frozenset([2]), frozenset([3])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
            frozenset([frozenset([1, 2, 3])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 4]]),
            frozenset([frozenset([1, 2, 3]), frozenset([1, 2, 4])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 4]]),
            frozenset([frozenset([1, 2, 3]), frozenset([1, 2, 4])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 4], [1, 2, 4]]),
            frozenset([frozenset([1, 2, 3]), frozenset([1, 2, 4])])
        )

    def test_special_cases(self):
        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [1, 2, 3], [3, 2, 1]]),
            frozenset([frozenset([1, 2, 3])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [1, 2, -3], [1, 2, 3]]),
            frozenset([frozenset([1, 2, 3]), frozenset([1, 2, -3])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [1, 2, 3], [1, 2, 4], [1, 2, 4, 5]]),
            frozenset([frozenset([1, 2, 3]), frozenset([1, 2, 4])])
        )

        self.assertCountEqual(
            remove_similar_row([[1, 2, 3], [1, 2