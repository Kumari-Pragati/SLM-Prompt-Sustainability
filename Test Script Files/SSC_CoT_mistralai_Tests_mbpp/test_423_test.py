import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_normal_input(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(get_maxgold(gold, 3, 3), 9)

    def test_edge_case_top(self):
        gold = [[1], [2]]
        self.assertEqual(get_maxgold(gold, 2, 1), 2)

    def test_edge_case_bottom(self):
        gold = [[1, 2, 3], [4]]
        self.assertEqual(get_maxgold(gold, 2, 1), 4)

    def test_edge_case_left(self):
        gold = [[1], [2, 3]]
        self.assertEqual(get_maxgold(gold, 1, 2), 3)

    def test_edge_case_right(self):
        gold = [[1, 2], [3]]
        self.assertEqual(get_maxgold(gold, 2, 1), 3)

    def test_edge_case_single_row(self):
        gold = [[1]]
        self.assertEqual(get_maxgold(gold, 1, 1), 1)

    def test_edge_case_single_column(self):
        gold = [[1], [2]]
        self.assertEqual(get_maxgold(gold, 2, 1), 2)

    def test_invalid_input_dimensions(self):
        with self.assertRaises(ValueError):
            get_maxgold(gold=[[1, 2, 3]], m=2, n=1)
