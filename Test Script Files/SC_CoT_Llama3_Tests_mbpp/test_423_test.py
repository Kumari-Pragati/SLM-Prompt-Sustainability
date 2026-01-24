import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):
    def test_typical_input(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 9)

    def test_edge_case_m1(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 1
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 1)

    def test_edge_case_n1(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 1
        self.assertEqual(get_maxgold(gold, m, n), 1)

    def test_edge_case_m1_n1(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 1
        n = 1
        self.assertEqual(get_maxgold(gold, m, n), 1)

    def test_corner_case(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 9)

    def test_invalid_input_m0(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 0
        n = 3
        with self.assertRaises(IndexError):
            get_maxgold(gold, m, n)

    def test_invalid_input_n0(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 0
        with self.assertRaises(IndexError):
            get_maxgold(gold, m, n)

    def test_invalid_input_m0_n0(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 0
        n = 0
        with self.assertRaises(IndexError):
            get_maxgold(gold, m, n)
