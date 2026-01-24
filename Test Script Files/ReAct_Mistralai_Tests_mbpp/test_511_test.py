import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_find_min_sum_positive_numbers(self):
        self.assertEqual(find_Min_Sum(6), 2)
        self.assertEqual(find_Min_Sum(12), 3)
        self.assertEqual(find_Min_Sum(20), 4)
        self.assertEqual(find_Min_Sum(28), 6)
        self.assertEqual(find_Min_Sum(496), 8)

    def test_find_min_sum_zero(self):
        self.assertEqual(find_Min_Sum(0), 0)

    def test_find_min_sum_negative_numbers(self):
        self.assertEqual(find_Min_Sum(-6), 2)
        self.assertEqual(find_Min_Sum(-12), 3)
        self.assertEqual(find_Min_Sum(-20), 4)
        self.assertEqual(find_Min_Sum(-28), 6)
        self.assertEqual(find_Min_Sum(-496), 8)

    def test_find_min_sum_prime_numbers(self):
        self.assertEqual(find_Min_Sum(5), 5)
        self.assertEqual(find_Min_Sum(7), 7)
        self.assertEqual(find_Min_Sum(11), 11)
        self.assertEqual(find_Min_Sum(13), 13)
        self.assertEqual(find_Min_Sum(17), 17)

    def test_find_min_sum_large_numbers(self):
        self.assertEqual(find_Min_Sum(1000000), 1000000)
        self.assertEqual(find_Min_Sum(1000000000), 1000000000)
