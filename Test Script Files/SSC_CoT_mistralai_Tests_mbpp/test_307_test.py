import unittest
from mbpp_307_code import deepcopy
from thirty_seven_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_normal_case(self):
        tuplex = ((1, 2), (3, 4), (5, 6))
        result = colon_tuplex(tuplex, 1, 7)
        self.assertListEqual(result, ((1, 2, 7), (3, 4), (5, 6)))

    def test_edge_case_empty_list(self):
        tuplex = ((), (3, 4), (5, 6))
        result = colon_tuplex(tuplex, 1, 7)
        self.assertListEqual(result, ((1, 7), (3, 4), (5, 6)))

    def test_edge_case_last_index(self):
        tuplex = ((1, 2), (3, 4), (5, 6, 8))
        result = colon_tuplex(tuplex, 2, 7)
        self.assertListEqual(result, ((1, 2), (3, 4, 7), (5, 6, 8)))

    def test_edge_case_negative_index(self):
        tuplex = ((1, 2), (3, 4), (5, 6))
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, -1, 7)

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            colon_tuplex(123, 1, 7)

    def test_invalid_input_type_tuple(self):
        with self.assertRaises(TypeError):
            colon_tuplex([1, 2], 'a', 7)
