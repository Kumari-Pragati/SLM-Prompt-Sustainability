import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):
    def test_typical_case(self):
        tuplex = [{'a': 1}, {'b': 2}]
        result = colon_tuplex(tuplex, 0, 3)
        self.assertEqual(result, [{'a': 1}, {'b': 2}, {'a': 3}])

    def test_edge_case(self):
        tuplex = [{'a': 1}]
        result = colon_tuplex(tuplex, 0, 3)
        self.assertEqual(result, [{'a': 1}, {'a': 3}])

    def test_edge_case2(self):
        tuplex = [{'a': 1, 'b': 2}]
        result = colon_tuplex(tuplex, 1, 3)
        self.assertEqual(result, [{'a': 1, 'b': 2}, {'b': 3}])

    def test_edge_case3(self):
        tuplex = []
        result = colon_tuplex(tuplex, 0, 3)
        self.assertEqual(result, [])

    def test_edge_case4(self):
        tuplex = [{'a': 1}]
        result = colon_tuplex(tuplex, 0, 1)
        self.assertEqual(result, [{'a': 1}])

    def test_edge_case5(self):
        tuplex = [{'a': 1, 'b': 2}]
        result = colon_tuplex(tuplex, 0, 1)
        self.assertEqual(result, [{'a': 1, 'b': 2}])
