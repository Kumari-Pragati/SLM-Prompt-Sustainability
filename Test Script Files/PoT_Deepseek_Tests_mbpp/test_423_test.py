import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_typical_case(self):
        gold = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 12)

    def test_edge_case_single_column(self):
        gold = [[1], [2], [3]]
        m = 3
        n = 1
        self.assertEqual(get_maxgold(gold, m, n), 6)

    def test_boundary_case_empty_gold(self):
        gold = []
        m = 0
        n = 0
        self.assertEqual(get_maxgold(gold, m, n), 0)

    def test_corner_case_all_same_values(self):
        gold = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 9)

    def test_corner_case_all_different_values(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 33)
