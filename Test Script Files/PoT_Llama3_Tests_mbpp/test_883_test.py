import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 2, 3), [12, 6, 24, 18, 20, 30, 36, 60, 72, 100])

    def test_edge_case_m_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 0, 3), [12, 6, 24, 18, 20, 30, 36, 60, 72, 100])

    def test_edge_case_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 2, 0), [])

    def test_edge_case_m_and_n_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 0, 0), [])

    def test_edge_case_m_and_n_one(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 1, 1), [])

    def test_edge_case_m_and_n_negative(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], -2, -3), [])

    def test_edge_case_m_and_n_zero_and_negative(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], 0, -3), [])

    def test_edge_case_m_and_n_negative_and_zero(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60, 72, 75, 80, 90, 100], -2, 0), [])
