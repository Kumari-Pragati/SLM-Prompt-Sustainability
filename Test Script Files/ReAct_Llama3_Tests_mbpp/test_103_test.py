import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_zero_n(self):
        self.assertEqual(eulerian_num(0, 0), 1)

    def test_zero_m(self):
        self.assertEqual(eulerian_num(1, 0), 1)

    def test_n_greater_than_m(self):
        self.assertEqual(eulerian_num(5, 3), 0)

    def test_m_greater_than_n(self):
        self.assertEqual(eulerian_num(3, 5), 0)

    def test_recursive_calls(self):
        self.assertEqual(eulerian_num(4, 2), 3)

    def test_edge_case_n_zero(self):
        self.assertEqual(eulerian_num(0, 1), 0)

    def test_edge_case_m_zero(self):
        self.assertEqual(eulerian_num(1, 0), 1)
