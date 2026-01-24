import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxgold(unittest.TestCase):
    def test_typical_use_case(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m, n = len(gold), len(gold[0])
        self.assertEqual(get_maxgold(gold, m, n), 9)

    def test_empty_gold_table(self):
        gold = []
        with self.assertRaises(ValueError):
            get_maxgold(gold, 0, 0)

    def test_single_row_gold_table(self):
        gold = [[1]]
        with self.assertRaises(ValueError):
            get_maxgold(gold, 1, 1)

    def test_single_column_gold_table(self):
        gold = [[1]] * 5
        with self.assertRaises(ValueError):
            get_maxgold(gold, 1, len(gold))

    def test_negative_gold_values(self):
        gold = [[-1, 2, 3], [-4, -5, -6], [-7, -8, -9]]
        m, n = len(gold), len(gold[0])
        self.assertEqual(get_maxgold(gold, m, n), -9)

    def test_zero_gold_values(self):
        gold = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        m, n = len(gold), len(gold[0])
        self.assertEqual(get_maxgold(gold, m, n), 0)
