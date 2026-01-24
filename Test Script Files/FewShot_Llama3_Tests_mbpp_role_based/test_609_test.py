import unittest
from mbpp_609_code import floor_Min

class TestFloor_Min(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(floor_Min(10, 5, 20), 20)

    def test_edge_case_N_is_zero(self):
        self.assertEqual(floor_Min(10, 5, 0), 0)

    def test_edge_case_B_is_one(self):
        self.assertEqual(floor_Min(10, 1, 20), 10)

    def test_edge_case_A_is_zero(self):
        self.assertEqual(floor_Min(0, 5, 20), 0)

    def test_edge_case_B_is_zero(self):
        with self.assertRaises(ZeroDivisionError):
            floor_Min(10, 0, 20)

    def test_edge_case_N_is_negative(self):
        with self.assertRaises(ValueError):
            floor_Min(10, 5, -20)
