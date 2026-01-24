import unittest
from mbpp_142_code import count_samepair

class TestCountSamePair(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(count_samepair([1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3]), 3)

    def test_edge_case_equal_lengths(self):
        self.assertEqual(count_samepair([1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 4]), 3)

    def test_edge_case_different_lengths(self):
        self.assertEqual(count_samepair([1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 4, 5]), 3)

    def test_edge_case_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_samepair([1], [1], [1]), 1)

    def test_edge_case_no_matches(self):
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, count_samepair, [1, 2, 3], 'a', 'b')
        self.assertRaises(TypeError, count_samepair, 'a', [1, 2, 3], 'b')
        self.assertRaises(TypeError, count_samepair, 'a', 'b', [1, 2, 3])
