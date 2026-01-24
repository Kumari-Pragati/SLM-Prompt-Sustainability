import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_case_A_1(self):
        self.assertEqual(count_no(1, 2, 3, 5), 5)

    def test_edge_case_A_2(self):
        self.assertEqual(count_no(2, 2, 3, 5), 5)

    def test_edge_case_N_1(self):
        self.assertEqual(count_no(2, 1, 3, 5), 3)

    def test_edge_case_N_2(self):
        self.assertEqual(count_no(2, 2, 3, 5), 5)

    def test_edge_case_L_R_equal(self):
        self.assertEqual(count_no(2, 2, 3, 3), 3)

    def test_edge_case_L_R_equal_N_1(self):
        self.assertEqual(count_no(2, 1, 3, 3), 3)

    def test_edge_case_L_R_equal_N_2(self):
        self.assertEqual(count_no(2, 2, 3, 3), 3)

    def test_invalid_input_A_0(self):
        with self.assertRaises(TypeError):
            count_no(0, 2, 3, 5)

    def test_invalid_input_N_0(self):
        with self.assertRaises(TypeError):
            count_no(2, 0, 3, 5)

    def test_invalid_input_L_R_equal(self):
        with self.assertRaises(TypeError):
            count_no(2, 2, 3, 3)
