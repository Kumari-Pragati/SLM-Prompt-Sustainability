import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):
    def test_typical_case(self):
        gold = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 12)

    def test_edge_case(self):
        gold = [[1]]
        m = 1
        n = 1
        self.assertEqual(get_maxgold(gold, m, n), 1)

    def test_boundary_case(self):
        gold = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 0)

    def test_invalid_input(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        m = 2
        n = 3
        with self.assertRaises(Exception):
            get_maxgold(gold, m, n)
