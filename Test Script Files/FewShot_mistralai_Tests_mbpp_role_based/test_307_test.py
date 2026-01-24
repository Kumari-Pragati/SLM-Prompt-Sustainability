import unittest
from mbpp_307_code import deepcopy
from thirty_seven_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):
    def test_valid_input(self):
        tuplex = [['a', 'b'], ['c', 'd']]
        result = colon_tuplex(tuplex, 0, 1)
        self.assertEqual(result, [['a', 'b', 1], ['c', 'd']])

        tuplex = [['a', 'b'], ['c', 'd']]
        result = colon_tuplex(tuplex, 1, 2)
        self.assertEqual(result, [['a', 'b'], ['c', 'd', 2]])

    def test_edge_case_first_index(self):
        tuplex = [['a', 'b']]
        result = colon_tuplex(tuplex, 0, 1)
        self.assertEqual(result, [['a', 'b', 1]])

    def test_edge_case_last_index(self):
        tuplex = [['a', 'b'], ['c', 'd']]
        result = colon_tuplex(tuplex, 1, 1)
        self.assertEqual(result, [['a', 'b'], ['c', 'd', 1]])

    def test_invalid_input_first_index(self):
        tuplex = [['a', 'b']]
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, -1, 1)

    def test_invalid_input_second_index(self):
        tuplex = [['a', 'b']]
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, 0, -1)
