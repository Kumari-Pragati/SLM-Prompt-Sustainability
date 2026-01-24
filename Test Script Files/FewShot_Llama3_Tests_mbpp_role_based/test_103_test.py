import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(eulerian_num(5, 3), 10)

    def test_edge_case_n_zero(self):
        self.assertEqual(eulerian_num(0, 3), 0)

    def test_edge_case_m_zero(self):
        self.assertEqual(eulerian_num(5, 0), 1)

    def test_edge_case_n_m_equal(self):
        self.assertEqual(eulerian_num(5, 5), 0)

    def test_edge_case_n_m_negative(self):
        with self.assertRaises(ValueError):
            eulerian_num(-1, -2)

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(eulerian_num(5, 6), 0)
