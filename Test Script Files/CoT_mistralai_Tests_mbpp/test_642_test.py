import unittest
from mbpp_642_code import set
from six.moves.range import range

from 642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_empty_list(self):
        self.assertSetEqual(set(), remove_similar_row([]))

    def test_single_element_list(self):
        for data in [
            ([(1, 2, 3)], {(1, 2, 3)}),
            ([('a', 'b', 'c')], {('a', 'b', 'c')}),
            ([{1, 2, 3}], {{1, 2, 3}}),
        ]:
            self.assertSetEqual(data[1], remove_similar_row(data[0]))

    def test_duplicate_elements(self):
        for data in [
            ([
                [(1, 2, 3)],
                [(1, 2, 3)],
                [(1, 2, 3)],
            ], {(1, 2, 3)}),
            ([
                [(1, 2, 3)],
                [(1, 2, 4)],
                [(1, 2, 3)],
            ], {(1, 2, 3), (1, 2, 4)}),
            ([
                [(1, 2, 3)],
                [(1, 2, 3), (1, 2, 3)],
                [(1, 2, 3)],
            ], {(1, 2, 3)}),
        ]:
            self.assertSetEqual(data[1], remove_similar_row(data[0]))

    def test_mixed_elements(self):
        for data in [
            ([
                [(1, 2, 3)],
                [(1, 2, 4)],
                [(1, 2, 3)],
            ], {(1, 2, 3), (1, 2, 4)}),
            ([
                [(1, 2, 3)],
                [(1, 2, 4), (1, 2, 3)],
                [(1, 2, 3)],
            ], {(1, 2, 3), (1, 2, 4)}),
            ([
                [(1, 2, 3)],
                [(1, 2, 4), (1, 2, 3), (1, 2, 3)],
                [(1, 2, 3)],
            ], {(1, 2, 3), (1, 2, 4)}),
        ]:
            self.assertSetEqual(data[1], remove_similar_row(data[0]))

    def test_empty_sublists(self):
        for data in [
            ([
                [],
                [(1, 2, 3)],
                [(1, 2, 3)],
            ], {(1, 2, 3)}),
            ([
                [(1, 2, 3)],
                [],
                [(1, 2, 3)],
            ], {(1, 2, 3)}),
            ([
                [(1, 2, 3)],
                [(1, 2, 3)],
                [],
            ], {(1, 2, 3)}),
        ]:
            self.assertSetEqual(data[1], remove_similar_row(data[0]))

    def test_invalid_input(self):
        for data in [
            (1, TypeError),
            ([], TypeError),
            ([1], TypeError),
            ([1, 2], TypeError),
            ([1, 2, 3], TypeError),
            ([1, 2, (1, 2, 3)], TypeError),
            ([1,