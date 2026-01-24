import unittest
from mbpp_307_code import deepcopy
from thirty_seven_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_empty_list(self):
        tuplex = []
        result = colon_tuplex(tuplex, 0, 1)
        self.assertEqual(result, [[1]])

    def test_single_list(self):
        tuplex = [[]]
        result = colon_tuplex(tuplex, 0, 1)
        self.assertEqual(result, [[1]])

    def test_multiple_lists(self):
        tuplex = [[], [2], [3]]
        result = colon_tuplex(tuplex, 1, 1)
        self.assertEqual(result, [[2], [1], [3]])

    def test_negative_index(self):
        tuplex = [[], [2], [3]]
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, -1, 1)

    def test_index_out_of_range(self):
        tuplex = [[], [2], [3]]
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, 2, 1)
