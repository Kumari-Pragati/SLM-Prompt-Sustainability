import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):
    def test_typical_use_case(self):
        tuplex = [{'a': 1}, {'b': 2}]
        result = colon_tuplex(tuplex, 'b', 3)
        self.assertEqual(result, [{'a': 1}, {'b': [2, 3]}])

    def test_edge_case_empty_tuplex(self):
        tuplex = []
        result = colon_tuplex(tuplex, 'a', 1)
        self.assertEqual(result, [{'a': [1]}])

    def test_edge_case_non_existent_key(self):
        tuplex = [{'a': 1}, {'b': 2}]
        result = colon_tuplex(tuplex, 'c', 3)
        self.assertEqual(result, [{'a': 1}, {'b': 2}])

    def test_edge_case_non_list_value(self):
        tuplex = [{'a': 1}, {'b': 2}]
        result = colon_tuplex(tuplex, 'b', 'three')
        self.assertEqual(result, [{'a': 1}, {'b': [2, 'three']}])

    def test_edge_case_list_value(self):
        tuplex = [{'a': 1}, {'b': 2}]
        result = colon_tuplex(tuplex, 'b', [2, 3, 4])
        self.assertEqual(result, [{'a': 1}, {'b': [2, 3, 4]}])
