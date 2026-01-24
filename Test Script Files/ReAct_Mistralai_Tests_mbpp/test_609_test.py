import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Min(3, 5, 10), 15)

    def test_edge_case_A_zero(self):
        self.assertEqual(floor_Min(0, 5, 10), 0)

    def test_edge_case_B_one(self):
        self.assertEqual(floor_Min(3, 1, 10), 0)

    def test_edge_case_N_zero(self):
        self.assertEqual(floor_Min(3, 5, 0), 0)

    def test_edge_case_N_equal_B_minus_one(self):
        self.assertEqual(floor_Min(3, 5, 4), 12)

    def test_edge_case_N_greater_than_B(self):
        self.assertEqual(floor_Min(3, 5, 6), 15)

    def test_negative_A(self):
        with self.assertRaises(ValueError):
            floor_Min(-3, 5, 10)

    def test_negative_B(self):
        with self.assertRaises(ValueError):
            floor_Min(3, -5, 10)
