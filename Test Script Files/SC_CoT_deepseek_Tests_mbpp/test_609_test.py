import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Min(5, 2, 3), 10)

    def test_boundary_case_A_zero(self):
        self.assertEqual(floor_Min(0, 2, 3), 0)

    def test_boundary_case_B_zero(self):
        self.assertEqual(floor_Min(5, 0, 3), 0)

    def test_edge_case_A_B_equal(self):
        self.assertEqual(floor_Min(5, 5, 3), 5)

    def test_edge_case_A_B_greater(self):
        self.assertEqual(floor_Min(5, 6, 3), 5)

    def test_edge_case_N_greater_than_B(self):
        self.assertEqual(floor_Min(5, 2, 4), 10)

    def test_edge_case_N_equal_to_B(self):
        self.assertEqual(floor_Min(5, 2, 2), 10)

    def test_edge_case_N_less_than_B(self):
        self.assertEqual(floor_Min(5, 2, 1), 10)

    def test_invalid_input_A_negative(self):
        with self.assertRaises(Exception):
            floor_Min(-5, 2, 3)

    def test_invalid_input_B_negative(self):
        with self.assertRaises(Exception):
            floor_Min(5, -2, 3)

    def test_invalid_input_N_negative(self):
        with self.assertRaises(Exception):
            floor_Min(5, 2, -3)
