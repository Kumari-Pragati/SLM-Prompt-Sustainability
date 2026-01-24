import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxGold(unittest.TestCase):

    def test_typical_case(self):
        gold = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 12)

    def test_edge_case_single_column(self):
        gold = [[5], [6], [7]]
        m = 3
        n = 1
        self.assertEqual(get_maxgold(gold, m, n), 26)

    def test_edge_case_single_row(self):
        gold = [[5, 6, 7]]
        m = 1
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 26)

    def test_edge_case_empty_gold(self):
        gold = []
        m = 0
        n = 0
        self.assertEqual(get_maxgold(gold, m, n), 0)

    def test_explicitly_handled_error_case(self):
        gold = None
        m = 0
        n = 0
        with self.assertRaises(TypeError):
            get_maxgold(gold, m, n)
