import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_find_min_sum_for_perfect_numbers(self):
        self.assertEqual(find_Min_Sum(6), 6)
        self.assertEqual(find_Min_Sum(28), 14)
        self.assertEqual(find_Min_Sum(496), 784)

    def test_find_min_sum_for_non_perfect_numbers(self):
        self.assertEqual(find_Min_Sum(10), 10)
        self.assertEqual(find_Min_Sum(15), 15)
        self.assertEqual(find_Min_Sum(20), 4)

    def test_find_min_sum_for_negative_numbers(self):
        self.assertEqual(find_Min_Sum(-6), -6)
        self.assertEqual(find_Min_Sum(-28), -28)
        self.assertEqual(find_Min_Sum(-496), -784)

    def test_find_min_sum_for_zero(self):
        self.assertEqual(find_Min_Sum(0), 0)
