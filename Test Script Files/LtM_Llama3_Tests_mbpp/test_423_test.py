import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxgold(unittest.TestCase):
    def test_simple(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 2
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 6)

    def test_edge_case1(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 2
        n = 1
        self.assertRaises(IndexError, get_maxgold, gold, m, n)

    def test_edge_case2(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 1
        n = 3
        self.assertRaises(IndexError, get_maxgold, gold, m, n)

    def test_edge_case3(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 0
        n = 3
        self.assertRaises(IndexError, get_maxgold, gold, m, n)

    def test_edge_case4(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 2
        n = 0
        self.assertRaises(IndexError, get_maxgold, gold, m, n)

    def test_edge_case5(self):
        gold = []
        m = 0
        n = 3
        self.assertRaises(IndexError, get_maxgold, gold, m, n)

    def test_edge_case6(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 2
        n = 0
        self.assertRaises(IndexError, get_maxgold, gold, m, n)
