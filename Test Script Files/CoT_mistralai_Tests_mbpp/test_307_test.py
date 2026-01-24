import unittest
from mbpp_307_code import deepcopy
from thirty_seven_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):
    def test_empty_tuple_list(self):
        self.assertEqual(colon_tuplex([], 0, 5), [(0, 5)])

    def test_single_tuple_list(self):
        self.assertEqual(colon_tuplex([(1, 2)], 0, 5), [(0, 5), (1, 2)])

    def test_multiple_tuple_list(self):
        self.assertEqual(colon_tuplex([(1, 2), (3, 4)], 0, 5), [(0, 5), (1, 2), (3, 4)])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            colon_tuplex([(1, 2)], -1, 5)

    def test_index_greater_than_length(self):
        with self.assertRaises(IndexError):
            colon_tuplex([(1, 2)], 2, 5)

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            colon_tuplex('not a tuple', 0, 5)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            colon_tuplex([(1, 2)], 0, 'five')
