import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Min_Sum(10), 10)
        self.assertEqual(find_Min_Sum(17), 17)
        self.assertEqual(find_Min_Sum(36), 36)
        self.assertEqual(find_Min_Sum(120), 120)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Sum(0), 0)
        self.assertEqual(find_Min_Sum(1), 1)

    def test_boundary_cases(self):
        self.assertEqual(find_Min_Sum(2), 2)
        self.assertEqual(find_Min_Sum(4), 4)
        self.assertEqual(find_Min_Sum(8), 8)
        self.assertEqual(find_Min_Sum(16), 16)

    def test_corner_cases(self):
        self.assertEqual(find_Min_Sum(9), 9)
        self.assertEqual(find_Min_Sum(25), 25)
        self.assertEqual(find_Min_Sum(49), 49)
        self.assertEqual(find_Min_Sum(81), 81)
