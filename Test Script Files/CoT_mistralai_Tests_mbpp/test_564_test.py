import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_Pairs([], 0), 0)

    def test_single_element(self):
        self.assertEqual(count_Pairs([1], 1), 0)

    def test_duplicates(self):
        self.assertEqual(count_Pairs([1, 1, 2, 2, 3, 3], 6), 3)

    def test_unique_elements(self):
        self.assertEqual(count_Pairs([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_first_element(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_edge_case_last_element(self):
        self.assertEqual(count_Pairs([1, 1, 2], 3), 1)

    def test_edge_case_only_two_elements(self):
        self.assertEqual(count_Pairs([1, 1], 2), 1)

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, count_Pairs, 'not a list', 0)

    def test_invalid_input_n(self):
        self.assertRaises(TypeError, count_Pairs, [1], 'not a number')
