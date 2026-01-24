import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_case_A_equals_1(self):
        self.assertEqual(count_no(1, 3, 5, 10), 5)

    def test_edge_case_A_equals_10(self):
        self.assertEqual(count_no(10, 3, 5, 10), 9)

    def test_edge_case_N_equals_1(self):
        self.assertEqual(count_no(2, 1, 5, 10), 5)

    def test_edge_case_N_equals_10(self):
        self.assertEqual(count_no(2, 10, 5, 10), 7)

    def test_edge_case_L_equals_R(self):
        self.assertEqual(count_no(2, 3, 5, 5), 5)

    def test_edge_case_L_greater_than_R(self):
        self.assertEqual(count_no(2, 3, 10, 5), 5)

    def test_invalid_input_A_zero(self):
        with self.assertRaises(ZeroDivisionError):
            count_no(0, 3, 5, 10)

    def test_invalid_input_N_zero(self):
        with self.assertRaises(ZeroDivisionError):
            count_no(2, 0, 5, 10)
