import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(floor_Max(1, 2, 3), 2)
        self.assertEqual(floor_Max(2, 3, 5), 6)
        self.assertEqual(floor_Max(3, 4, 7), 12)

    def test_zero_and_positive_numbers(self):
        self.assertEqual(floor_Max(1, 2, 0), 0)
        self.assertEqual(floor_Max(2, 3, 0), 0)
        self.assertEqual(floor_Max(3, 4, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(floor_Max(-1, -2, 3), 3)
        self.assertEqual(floor_Max(-2, -3, 5), 10)
        self.assertEqual(floor_Max(-3, -4, 7), 21)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(floor_Max(-1, 2, 3), 6)
        self.assertEqual(floor_Max(-2, 3, 5), 10)
        self.assertEqual(floor_Max(-3, 4, 7), 14)

    def test_edge_cases_A(self):
        self.assertEqual(floor_Max(1, 2, 1), 1)
        self.assertEqual(floor_Max(2, 3, 2), 6)
        self.assertEqual(floor_Max(3, 4, 3), 12)

    def test_edge_cases_B(self):
        self.assertEqual(floor_Max(1, 1, 2), 0)
        self.assertEqual(floor_Max(2, 2, 3), 4)
        self.assertEqual(floor_Max(3, 3, 4), 9)

    def test_edge_cases_N(self):
        self.assertEqual(floor_Max(1, 2, 0), 0)
        self.assertEqual(floor_Max(2, 3, 0), 0)
        self.assertEqual(floor_Max(3, 4, 0), 0)

    def test_error_cases_A_zero(self):
        with self.assertRaises(ValueError):
            floor_Max(0, 2, 3)

    def test_error_cases_B_zero(self):
        with self.assertRaises(ValueError):
            floor_Max(1, 0, 3)
