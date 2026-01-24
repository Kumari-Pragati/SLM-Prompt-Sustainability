import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxgold(unittest.TestCase):

    def test_typical_case(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(get_maxgold(gold, 3, 3), 9)

    def test_edge_case_top(self):
        gold = [[1], [2]]
        self.assertEqual(get_maxgold(gold, 2, 1), 2)

    def test_edge_case_bottom(self):
        gold = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(get_maxgold(gold, 2, 0), 6)

    def test_edge_case_left(self):
        gold = [[1, 2], [3, 4]]
        self.assertEqual(get_maxgold(gold, 2, 1), 4)

    def test_edge_case_right(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(get_maxgold(gold, 3, 2), 9)

    def test_empty_list(self):
        gold = []
        self.assertRaises(IndexError, get_maxgold, gold, 1, 1)

    def test_negative_dimensions(self):
        self.assertRaises(ValueError, get_maxgold, gold, -1, 1)
        self.assertRaises(ValueError, get_maxgold, gold, 1, -1)
