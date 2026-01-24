import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 5, 10), [10, 20, 30, 40])

    def test_edge_case_m_divides_all(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 10, 1), [10, 20, 30, 40])

    def test_edge_case_n_divides_all(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 1, 10), [10, 20, 30, 40])

    def test_boundary_case_m_and_n_equal(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 10, 10), [10, 20, 30, 40])

    def test_boundary_case_m_and_n_large(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 1000, 1000), [])

    def test_typical_case_m_not_divisor(self):
        self.assertEqual(div_of_nums([11, 22, 33, 44], 5, 10), [22, 33, 44])

    def test_typical_case_n_not_divisor(self):
        self.assertEqual(div_of_nums([11, 22, 33, 44], 1, 11), [22, 33, 44])

    def test_typical_case_no_divisors(self):
        self.assertEqual(div_of_nums([11, 22, 33, 44], 13, 17), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(div_of_nums([], 1, 10), [])

    def test_edge_case_m_zero(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 0, 10), [])

    def test_edge_case_n_zero(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 10, 0), [])

    def test_boundary_case_m_and_n_zero(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 0, 0), [])
