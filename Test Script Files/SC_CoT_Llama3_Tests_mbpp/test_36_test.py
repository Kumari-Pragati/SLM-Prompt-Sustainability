import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_Nth_Digit(123, 1, 1), 1)

    def test_edge_case_N_zero(self):
        self.assertEqual(find_Nth_Digit(123, 1, 0), None)

    def test_edge_case_p_zero(self):
        self.assertRaises(ZeroDivisionError, find_Nth_Digit, 0, 1, 1)

    def test_edge_case_q_zero(self):
        self.assertRaises(ZeroDivisionError, find_Nth_Digit, 123, 0, 1)

    def test_edge_case_N_large(self):
        self.assertEqual(find_Nth_Digit(123, 1, 1000), 3)

    def test_edge_case_p_large(self):
        self.assertEqual(find_Nth_Digit(123456789, 1, 1), 7)

    def test_edge_case_q_large(self):
        self.assertEqual(find_Nth_Digit(123, 123456789, 1), 1)

    def test_edge_case_N_negative(self):
        with self.assertRaises(ValueError):
            find_Nth_Digit(123, 1, -1)

    def test_edge_case_p_negative(self):
        with self.assertRaises(ValueError):
            find_Nth_Digit(-123, 1, 1)

    def test_edge_case_q_negative(self):
        with self.assertRaises(ValueError):
            find_Nth_Digit(123, -1, 1)
