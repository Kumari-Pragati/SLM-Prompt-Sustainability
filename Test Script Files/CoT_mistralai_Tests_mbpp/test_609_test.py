import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Min(3, 5, 10), 15)
        self.assertEqual(floor_Min(4, 6, 12), 24)
        self.assertEqual(floor_Min(5, 7, 14), 35)

    def test_edge_case_A_zero(self):
        self.assertEqual(floor_Min(0, 4, 4), 0)

    def test_edge_case_B_one(self):
        self.assertEqual(floor_Min(2, 1, 1), 0)

    def test_edge_case_N_greater_than_B(self):
        self.assertEqual(floor_Min(3, 2, 3), 3)
        self.assertEqual(floor_Min(4, 3, 4), 12)

    def test_invalid_input_A_negative(self):
        self.assertRaises(ValueError, floor_Min, -1, 2, 3)

    def test_invalid_input_B_zero(self):
        self.assertRaises(ValueError, floor_Min, 2, 0, 3)

    def test_invalid_input_N_less_than_zero(self):
        self.assertRaises(ValueError, floor_Min, 2, 3, -1)
