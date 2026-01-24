import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):
    
    def test_typical_case(self):
        gold = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 12)

    def test_edge_case_single_row(self):
        gold = [[1, 2, 3]]
        m = 1
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 6)

    def test_edge_case_single_column(self):
        gold = [[1], [2], [3]]
        m = 3
        n = 1
        self.assertEqual(get_maxgold(gold, m, n), 6)

    def test_edge_case_empty_gold(self):
        gold = []
        m = 0
        n = 0
        self.assertEqual(get_maxgold(gold, m, n), 0)

    def test_invalid_input_negative_gold(self):
        gold = [[-1, 3, 3], [2, -1, 4], [0, 6, 4]]
        m = 3
        n = 3
        with self.assertRaises(Exception):
            get_maxgold(gold, m, n)

    def test_invalid_input_non_integer_gold(self):
        gold = [['a', 3, 3], [2, 'b', 4], [0, 6, 4]]
        m = 3
        n = 3
        with self.assertRaises(Exception):
            get_maxgold(gold, m, n)
