import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(floor_Min(10, 2, 5), 9)

    def test_edge_case_N_equal_B_minus_1(self):
        self.assertEqual(floor_Min(10, 2, 2), 8)

    def test_edge_case_N_greater_than_B_minus_1(self):
        self.assertEqual(floor_Min(10, 2, 10), 9)

    def test_edge_case_B_equal_1(self):
        with self.assertRaises(ZeroDivisionError):
            floor_Min(10, 1, 5)

    def test_edge_case_A_equal_0(self):
        with self.assertRaises(ZeroDivisionError):
            floor_Min(0, 2, 5)

    def test_edge_case_B_equal_0(self):
        with self.assertRaises(ZeroDivisionError):
            floor_Min(10, 0, 5)
