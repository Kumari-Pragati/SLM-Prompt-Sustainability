import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])

    def test_edge_case_m_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 3), [1, 2, 3, 4, 5])

    def test_edge_case_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 3, 0), [3])

    def test_edge_case_m_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 0), [])

    def test_edge_case_m_n_negative(self):
        self.assertEqual(div_of_nums([-1, -2, -3, -4, -5], -2, -3), [])

    def test_edge_case_m_n_positive(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])

    def test_edge_case_m_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 0), [])

    def test_edge_case_m_n_negative(self):
        self.assertEqual(div_of_nums([-1, -2, -3, -4, -5], -2, -3), [])

    def test_edge_case_m_n_positive(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])

    def test_edge_case_m_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 0), [])

    def test_edge_case_m_n_negative(self):
        self.assertEqual(div_of_nums([-1, -2, -3, -4, -5], -2, -3), [])

    def test_edge_case_m_n_positive(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])

    def test_edge_case_m_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 0), [])

    def test_edge_case_m_n_negative(self):
        self.assertEqual(div_of_nums([-1, -2, -3, -4, -5], -2, -3), [])

    def test_edge_case_m_n_positive(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])

    def test_edge_case_m_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 0), [])

    def test_edge_case_m_n_negative(self):
        self.assertEqual(div_of_nums([-1, -2, -3, -4, -5], -2, -3), [])

    def test_edge_case_m_n_positive(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])

    def test_edge_case_m_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 0), [])

    def test_edge_case_m_n_negative(self):
        self.assertEqual(div_of_nums([-1, -2, -3, -4, -5], -2, -3), [])

    def test_edge_case_m_n_positive(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])

    def test_edge_case_m_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 0), [])

    def test_edge_case_m_n_negative(self):
        self.assertEqual(div_of_nums([-1, -2, -3, -4, -5], -2, -3), [])

    def test_edge_case_m_n_positive(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])

    def test_edge_case_m_n_zero(self):
        self.assertEqual(div_of