import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_edge_case_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(count_samepair([1], [1], [1]), 1)
        self.assertEqual(count_samepair([1], [2], [1]), 0)

    def test_corner_case_different_lengths(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2], [1, 2, 3]), 2)
        self.assertEqual(count_samepair([1, 2], [1, 2, 3], [1, 2, 3]), 2)

    def test_corner_case_all_same(self):
        self.assertEqual(count_samepair([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3)

    def test_corner_case_all_different(self):
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)
