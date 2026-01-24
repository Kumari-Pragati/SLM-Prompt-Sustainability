import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_no(2, 3, 1, 10), 6)

    def test_edge_case_N_equals_0(self):
        self.assertEqual(count_no(2, 0, 1, 10), 1)

    def test_boundary_case_L_equals_R(self):
        self.assertEqual(count_no(2, 1, 5, 5), 5)

    def test_corner_case_A_equals_1(self):
        self.assertEqual(count_no(1, 3, 1, 10), 10)

    def test_invalid_case_N_greater_than_count(self):
        self.assertEqual(count_no(2, 10, 1, 10), 10)

    def test_invalid_case_A_equals_0(self):
        self.assertEqual(count_no(0, 3, 1, 10), 1)
