import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):
    def test_gcd_of_two_numbers(self):
        self.assertEqual(get_gcd([2, 3]), 1)
        self.assertEqual(get_gcd([4, 6]), 2)
        self.assertEqual(get_gcd([15, 25]), 5)
        self.assertEqual(get_gcd([10, 20]), 10)

    def test_gcd_of_three_numbers(self):
        self.assertEqual(get_gcd([2, 3, 4]), 1)
        self.assertEqual(get_gcd([4, 6, 8]), 2)
        self.assertEqual(get_gcd([15, 25, 35]), 5)
        self.assertEqual(get_gcd([10, 20, 30]), 10)

    def test_gcd_of_multiple_numbers(self):
        self.assertEqual(get_gcd([2, 3, 4, 5]), 1)
        self.assertEqual(get_gcd([4, 6, 8, 12]), 4)
        self.assertEqual(get_gcd([15, 25, 35, 45]), 5)
        self.assertEqual(get_gcd([10, 20, 30, 40]), 10)

    def test_gcd_of_single_number(self):
        self.assertEqual(get_gcd([1]), 1)
        self.assertEqual(get_gcd([2]), 2)
        self.assertEqual(get_gcd([5]), 5)

    def test_gcd_of_empty_list(self):
        with self.assertRaises(IndexError):
            get_gcd([])
