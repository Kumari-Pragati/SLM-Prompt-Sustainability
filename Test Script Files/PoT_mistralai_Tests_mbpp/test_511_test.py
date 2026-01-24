import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find_Min_Sum(6), 2)
        self.assertEqual(find_Min_Sum(12), 3)
        self.assertEqual(find_Min_Sum(20), 4)
        self.assertEqual(find_Min_Sum(28), 6)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(2), 2)
        self.assertEqual(find_Min_Sum(3), 3)
        self.assertEqual(find_Min_Sum(4), 2)
        self.assertEqual(find_Min_Sum(5), 5)

    def test_boundary_cases(self):
        self.assertEqual(find_Min_Sum(0), 0)
        self.assertEqual(find_Min_Sum(1024), 17)
        self.assertEqual(find_Min_Sum(2 ** 31 - 1), 2 ** 31 - 1)
        self.assertEqual(find_Min_Sum(2 ** 31), 2 ** 31)
