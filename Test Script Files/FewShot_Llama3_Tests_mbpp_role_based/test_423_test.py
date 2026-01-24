import unittest
from mbpp_423_code import get_maxgold

class TestGetMaxgold(unittest.TestCase):
    def test_typical_use_case(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 3
        self.assertEqual(get_maxgold(gold, m, n), 9)

    def test_edge_case_m_zero(self):
        gold = [[1, 2, 3]]
        m = 0
        n = 3
        with self.assertRaises(IndexError):
            get_maxgold(gold, m, n)

    def test_edge_case_n_zero(self):
        gold = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = 3
        n = 0
        with self.assertRaises(IndexError):
            get_maxgold(gold, m, n)

    def test_edge_case_m_n_zero(self):
        gold = [[1, 2, 3]]
        m = 0
        n = 0
        with self.assertRaises(IndexError):
            get_maxgold(gold, m, n)

    def test_invalid_input_type(self):
        gold = "Invalid input"
        m = 3
        n = 3
        with self.assertRaises(TypeError):
            get_maxgold(gold, m, n)
