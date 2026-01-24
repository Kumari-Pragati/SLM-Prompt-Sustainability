import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_Min_Sum(6), 2)
        self.assertEqual(find_Min_Sum(12), 3)
        self.assertEqual(find_Min_Sum(20), 4)
        self.assertEqual(find_Min_Sum(28), 6)
        self.assertEqual(find_Min_Sum(496), 8)

    def test_zero(self):
        self.assertEqual(find_Min_Sum(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Sum(-6), 6)
        self.assertEqual(find_Min_Sum(-12), 12)
        self.assertEqual(find_Min_Sum(-20), 20)
        self.assertEqual(find_Min_Sum(-28), 28)
        self.assertEqual(find_Min_Sum(-496), 496)

    def test_one(self):
        self.assertEqual(find_Min_Sum(1), 1)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Sum(1024), 16)
        self.assertEqual(find_Min_Sum(2147483647), 2147483647)
        self.assertEqual(find_Min_Sum(2 ** 64), 2 ** 64)
