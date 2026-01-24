import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Nth_Digit(10, 3, 2), 3)

    def test_edge_case_N_zero(self):
        self.assertEqual(find_Nth_Digit(10, 3, 0), 10)

    def test_edge_case_N_negative(self):
        with self.assertRaises(ValueError):
            find_Nth_Digit(10, 3, -1)

    def test_edge_case_p_zero(self):
        self.assertEqual(find_Nth_Digit(0, 3, 2), 0)

    def test_edge_case_q_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_Nth_Digit(10, 0, 2)

    def test_edge_case_large_N(self):
        self.assertEqual(find_Nth_Digit(10, 3, 1000), 0)

    def test_edge_case_large_p(self):
        self.assertEqual(find_Nth_Digit(10**100, 3, 2), 3)

    def test_edge_case_large_q(self):
        self.assertEqual(find_Nth_Digit(10, 3**100, 2), 3)
