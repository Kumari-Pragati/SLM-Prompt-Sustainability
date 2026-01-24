import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Min(10, 3, 2), 20)

    def test_edge_case_B_minus_1(self):
        self.assertEqual(floor_Min(5, 1, 2), 10)

    def test_edge_case_N(self):
        self.assertEqual(floor_Min(5, 3, 0), 0)

    def test_edge_case_B_equals_1(self):
        self.assertEqual(floor_Min(10, 1, 2), 10)

    def test_invalid_input_B_equals_0(self):
        with self.assertRaises(ZeroDivisionError):
            floor_Min(10, 0, 2)

    def test_invalid_input_negative_values(self):
        self.assertEqual(floor_Min(-10, -3, -2), -20)
