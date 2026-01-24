import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_no(2, 3, 5, 10), 7)

    def test_edge_case_A_1(self):
        self.assertEqual(count_no(1, 2, 5, 10), 9)

    def test_edge_case_A_5(self):
        self.assertEqual(count_no(5, 2, 5, 10), 7)

    def test_edge_case_N_1(self):
        self.assertEqual(count_no(2, 1, 5, 10), 5)

    def test_edge_case_N_5(self):
        self.assertEqual(count_no(2, 5, 5, 10), 7)

    def test_invalid_input_A_negative(self):
        with self.assertRaises(ValueError):
            count_no(-1, 2, 5, 10)

    def test_invalid_input_N_negative(self):
        with self.assertRaises(ValueError):
            count_no(2, -1, 5, 10)

    def test_invalid_input_L_greater_than_R(self):
        with self.assertRaises(ValueError):
            count_no(2, 2, 10, 5)
