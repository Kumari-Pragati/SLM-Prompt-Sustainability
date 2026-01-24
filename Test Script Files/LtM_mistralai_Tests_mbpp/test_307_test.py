import unittest
from mbpp_307_code import deepcopy
from 307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_simple(self):
        tuplex = ((1, 2), (3, 4))
        result = colon_tuplex(tuplex, 0, 5)
        self.assertEqual(result, ((1, 2, 5), (3, 4)))

        tuplex = ((1, 2), (3, 4))
        result = colon_tuplex(tuplex, 1, 5)
        self.assertEqual(result, ((1, 2), (3, 4, 5)))

    def test_edge_cases(self):
        tuplex = ((1, 2),)
        result = colon_tuplex(tuplex, 0, 5)
        self.assertEqual(result, ((1, 2, 5)))

        tuplex = ((1, 2),)
        result = colon_tuplex(tuplex, 0, 0)
        self.assertEqual(result, ((1, 2)))

        tuplex = ((1, 2), (3, 4))
        result = colon_tuplex(tuplex, -1, 5)
        self.assertEqual(result, ((1, 2), (3, 4, 5)))

        tuplex = ((1, 2), (3, 4))
        result = colon_tuplex(tuplex, 2, -1)
        self.assertEqual(result, ((1, 2), (3), (4)))

    def test_complex(self):
        tuplex = ((1, 2), (3, 4), (5, 6))
        result = colon_tuplex(tuplex, 1, 7)
        self.assertEqual(result, ((1, 2), (3, 4, 7), (5, 6)))

        tuplex = ((1, 2), (3, 4), (5, 6))
        result = colon_tuplex(tuplex, 2, 7)
        self.assertEqual(result, ((1, 2), (3), (5, 6, 7)))
