import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Sum(12), 10)

    def test_large_number(self):
        self.assertEqual(find_Min_Sum(100), 100)

    def test_small_number(self):
        self.assertEqual(find_Min_Sum(2), 2)

    def test_prime_number(self):
        self.assertEqual(find_Min_Sum(13), 13)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            find_Min_Sum(-12)

    def test_zero(self):
        self.assertEqual(find_Min_Sum(0), 0)

    def test_non_integer(self):
        with self.assertRaises(Exception):
            find_Min_Sum(12.5)

    def test_string(self):
        with self.assertRaises(Exception):
            find_Min_Sum('12')
