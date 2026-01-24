import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxgold(unittest.TestCase):
    def test_typical_case(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 9)

    def test_edge_case1(self):
        gold = [[1, 2], [3, 4]]
        m = 2
        n = 2
        self.assertEqual(get_maxgold(gold, m, n), 4)

    def test_edge_case2(self):
        gold = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        m = 2
        n = 5
        self.assertEqual(get_maxgold(gold, m, n), 10)

    def test_edge_case3(self):
        gold = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
        m = 1
        n = 15
        self.assertEqual(get_maxgold(gold, m, n), 15)

    def test_invalid_input1(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 0
        n = 3
        with self.assertRaises(IndexError):
            get_maxgold(gold, m, n)

    def test_invalid_input2(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 3
        n = 0
        with self.assertRaises(IndexError):
            get_maxgold(gold, m, n)
