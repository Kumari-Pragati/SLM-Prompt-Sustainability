import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_edge_case_all_equal(self):
        self.assertEqual(count_samepair([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3)

    def test_edge_case_all_diff(self):
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)

    def test_edge_case_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_edge_case_single_element_lists(self):
        self.assertEqual(count_samepair([1], [1], [1]), 1)

    def test_edge_case_single_element_lists_diff(self):
        self.assertEqual(count_samepair([1], [2], [3]), 0)

    def test_edge_case_single_element_lists_all_diff(self):
        self.assertEqual(count_samepair([1], [2, 3], [4, 5, 6]), 0)
