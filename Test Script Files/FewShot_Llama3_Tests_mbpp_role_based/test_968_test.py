import unittest
from mbpp_968_code import floor_Max

class TestFloor_Max(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(floor_Max(10, 5, 10), 4)

    def test_edge_case_A_zero(self):
        self.assertEqual(floor_Max(0, 5, 10), 0)

    def test_edge_case_B_one(self):
        self.assertEqual(floor_Max(10, 1, 10), 10)

    def test_edge_case_N_zero(self):
        self.assertEqual(floor_Max(10, 5, 0), 0)

    def test_edge_case_N_one(self):
        self.assertEqual(floor_Max(10, 5, 1), 0)

    def test_invalid_input_A_negative(self):
        with self.assertRaises(ValueError):
            floor_Max(-10, 5, 10)

    def test_invalid_input_B_negative(self):
        with self.assertRaises(ValueError):
            floor_Max(10, -5, 10)

    def test_invalid_input_N_negative(self):
        with self.assertRaises(ValueError):
            floor_Max(10, 5, -10)
