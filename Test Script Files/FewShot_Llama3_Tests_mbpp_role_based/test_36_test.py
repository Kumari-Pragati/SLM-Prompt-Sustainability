import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Nth_Digit(123, 3, 1), 3)

    def test_edge_case_N_zero(self):
        self.assertEqual(find_Nth_Digit(123, 3, 0), 1)

    def test_edge_case_N_equal_to_p_length(self):
        self.assertEqual(find_Nth_Digit(123, 3, 3), 3)

    def test_edge_case_q_one(self):
        self.assertEqual(find_Nth_Digit(123, 1, 1), 2)

    def test_edge_case_p_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_Nth_Digit(0, 3, 1)

    def test_edge_case_q_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_Nth_Digit(123, 0, 1)
