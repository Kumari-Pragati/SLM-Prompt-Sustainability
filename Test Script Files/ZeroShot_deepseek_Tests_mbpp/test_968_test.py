import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(floor_Max(3, 5, 10), 6)
        self.assertEqual(floor_Max(4, 7, 20), 20)
        self.assertEqual(floor_Max(2, 3, 15), 10)

    def test_negative_numbers(self):
        self.assertEqual(floor_Max(-3, -5, 10), -6)
        self.assertEqual(floor_Max(-4, -7, 20), -20)
        self.assertEqual(floor_Max(-2, -3, 15), -10)

    def test_zero(self):
        self.assertEqual(floor_Max(0, 5, 10), 0)
        self.assertEqual(floor_Max(0, 0, 20), 0)

    def test_max_limit(self):
        self.assertEqual(floor_Max(3, 5, 1000000000), 2000000000)

    def test_min_limit(self):
        self.assertEqual(floor_Max(3, 5, 0), 0)

    def test_equal_numbers(self):
        self.assertEqual(floor_Max(5, 5, 10), 10)

    def test_large_numbers(self):
        self.assertEqual(floor_Max(1000000000, 1000000000, 1000000000000000000), 1000000000000000000)
