import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_simple_positive_values(self):
        self.assertEqual(find_Volume(1, 2, 3), 6)
        self.assertEqual(find_Volume(4, 5, 6), 120)

    def test_edge_cases(self):
        self.assertEqual(find_Volume(0, 2, 3), 0)
        self.assertEqual(find_Volume(1, 0, 3), 0)
        self.assertEqual(find_Volume(1, 2, 0), 0)
        self.assertEqual(find_Volume(1, 1, 1), 1)

    def test_negative_values(self):
        self.assertEqual(find_Volume(-1, 2, 3), 0)
        self.assertEqual(find_Volume(1, -2, 3), 0)
        self.assertEqual(find_Volume(1, 2, -3), 0)

    def test_large_values(self):
        self.assertEqual(find_Volume(1e6, 2e6, 3e6), 4.188790204724e18)
