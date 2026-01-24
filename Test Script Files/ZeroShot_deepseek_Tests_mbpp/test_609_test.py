import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(floor_Min(5, 3, 2), 5)
        self.assertEqual(floor_Min(10, 4, 3), 10)
        self.assertEqual(floor_Min(15, 6, 4), 15)

    def test_negative_numbers(self):
        self.assertEqual(floor_Min(-5, 3, 2), -5)
        self.assertEqual(floor_Min(-10, 4, 3), -10)
        self.assertEqual(floor_Min(-15, 6, 4), -15)

    def test_zero_and_negative(self):
        self.assertEqual(floor_Min(0, 3, 2), 0)
        self.assertEqual(floor_Min(0, 4, 3), 0)
        self.assertEqual(floor_Min(0, 6, 4), 0)

    def test_large_numbers(self):
        self.assertEqual(floor_Min(1000000000, 1000000, 100000), 1000000000)
        self.assertEqual(floor_Min(2000000000, 2000000, 200000), 2000000000)
        self.assertEqual(floor_Min(3000000000, 3000000, 300000), 3000000000)

    def test_edge_cases(self):
        self.assertEqual(floor_Min(1, 1, 0), 1)
        self.assertEqual(floor_Min(0, 1, 0), 0)
        self.assertEqual(floor_Min(0, 0, 0), 0)
