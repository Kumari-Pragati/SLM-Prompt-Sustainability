import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):
    def test_simple(self):
        tuplex = [[1, 2], [3, 4]]
        m = 0
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_edge(self):
        tuplex = []
        m = 0
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [[5]])

    def test_edge2(self):
        tuplex = [[1, 2]]
        m = 0
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [[1, 2], [5]])

    def test_edge3(self):
        tuplex = [[1, 2], [3, 4]]
        m = 1
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_edge4(self):
        tuplex = [[1, 2], [3, 4]]
        m = 0
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_edge5(self):
        tuplex = [[1, 2], [3, 4]]
        m = 1
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_edge6(self):
        tuplex = [[1, 2], [3, 4]]
        m = 0
        n = 5
        result = colon_tuplex(tuplex, m, n)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])
