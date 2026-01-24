import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Max(2, 3, 10), 6)

    def test_edge_case_B_minus_1_greater_than_N(self):
        self.assertEqual(floor_Max(2, 3, 2), 4)

    def test_edge_case_B_minus_1_equal_to_N(self):
        self.assertEqual(floor_Max(2, 3, 3), 6)

    def test_edge_case_B_minus_1_less_than_N(self):
        self.assertEqual(floor_Max(2, 3, 4), 6)

    def test_invalid_input_A_zero(self):
        with self.assertRaises(ZeroDivisionError):
            floor_Max(0, 3, 4)

    def test_invalid_input_B_zero(self):
        with self.assertRaises(ZeroDivisionError):
            floor_Max(2, 0, 4)

    def test_invalid_input_N_negative(self):
        with self.assertRaises(ValueError):
            floor_Max(2, 3, -1)
