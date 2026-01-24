import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_no(2, 3, 1, 5), 4)

    def test_edge_case_A_equal_to_i(self):
        self.assertEqual(count_no(1, 2, 1, 5), 3)

    def test_edge_case_R_equal_to_L(self):
        self.assertEqual(count_no(2, 1, 1, 1), 1)

    def test_edge_case_N_equal_to_zero(self):
        self.assertEqual(count_no(2, 0, 1, 5), 1)

    def test_edge_case_N_greater_than_R_L(self):
        self.assertEqual(count_no(2, 5, 1, 5), 5)

    def test_edge_case_A_divides_i(self):
        self.assertEqual(count_no(2, 2, 1, 5), 4)

    def test_edge_case_A_divides_i_and_count_equal_to_N(self):
        self.assertEqual(count_no(2, 2, 1, 4), 4)

    def test_edge_case_A_divides_i_and_count_greater_than_N(self):
        self.assertEqual(count_no(2, 3, 1, 6), 6)
