import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(floor_Max(1, 2, 3), 2)
        self.assertEqual(floor_Max(2, 3, 4), 6)
        self.assertEqual(floor_Max(3, 4, 5), 12)

    def test_zero(self):
        self.assertEqual(floor_Max(0, 1, 0), 0)
        self.assertEqual(floor_Max(1, 0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(floor_Max(-1, -2, 1), -2)
        self.assertEqual(floor_Max(-2, -3, 2), 4)
        self.assertEqual(floor_Max(-3, -4, 3), 12)

    def test_negative_B(self):
        self.assertEqual(floor_Max(1, 2, -3), -6)
        self.assertEqual(floor_Max(2, 3, -4), -12)
        self.assertEqual(floor_Max(3, 4, -5), -24)

    def test_N_greater_than_B(self):
        self.assertEqual(floor_Max(1, 2, 3), 2)
        self.assertEqual(floor_Max(2, 3, 4), 2)
        self.assertEqual(floor_Max(3, 4, 5), 3)
