import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_no(3, 2, 1, 10), 9)

    def test_edge_case_A_1(self):
        self.assertEqual(count_no(1, 2, 1, 10), 2)

    def test_edge_case_A_10(self):
        self.assertEqual(count_no(10, 2, 1, 10), 9)

    def test_edge_case_N_1(self):
        self.assertEqual(count_no(3, 1, 1, 10), 3)

    def test_edge_case_N_10(self):
        self.assertEqual(count_no(3, 10, 1, 10), 9)

    def test_invalid_input_A_0(self):
        with self.assertRaises(ValueError):
            count_no(0, 2, 1, 10)

    def test_invalid_input_N_0(self):
        with self.assertRaises(ValueError):
            count_no(3, 0, 1, 10)

    def test_invalid_input_L_R_not_increasing(self):
        with self.assertRaises(ValueError):
            count_no(3, 2, 10, 1)
