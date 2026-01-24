import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_difference(3), 22)
        self.assertEqual(sum_difference(5), 100)
        self.assertEqual(sum_difference(10), 385)

    def test_edge_case(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(2), 8)
        self.assertEqual(sum_difference(4), 48)

    def test_corner_case(self):
        self.assertEqual(sum_difference(0), 0)
