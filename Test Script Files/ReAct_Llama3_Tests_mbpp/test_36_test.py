import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Nth_Digit(123, 3, 2), 3)

    def test_edge_case_N_zero(self):
        self.assertEqual(find_Nth_Digit(123, 3, 0), 1)

    def test_edge_case_p_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_Nth_Digit(0, 3, 2)

    def test_edge_case_q_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_Nth_Digit(123, 0, 2)

    def test_edge_case_N_large(self):
        self.assertEqual(find_Nth_Digit(123, 3, 100), 3)

    def test_edge_case_p_large(self):
        self.assertEqual(find_Nth_Digit(123456, 3, 2), 6)

    def test_edge_case_q_large(self):
        self.assertEqual(find_Nth_Digit(123, 345, 2), 3)
