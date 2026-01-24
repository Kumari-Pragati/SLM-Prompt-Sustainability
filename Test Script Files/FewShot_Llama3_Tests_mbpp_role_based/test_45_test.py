import unittest
from mbpp_45_code import get_gcd

class TestGetGcd(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(get_gcd([1]), 1)

    def test_two_element_list(self):
        self.assertEqual(get_gcd([2, 3]), 1)

    def test_three_element_list(self):
        self.assertEqual(get_gcd([4, 6, 8]), 2)

    def test_four_element_list(self):
        self.assertEqual(get_gcd([12, 15, 18, 21]), 3)

    def test_list_with_duplicates(self):
        self.assertEqual(get_gcd([2, 4, 6, 8]), 2)

    def test_list_with_negative_numbers(self):
        self.assertEqual(get_gcd([-12, 15, 18, 21]), 3)

    def test_list_with_mixed_signs(self):
        self.assertEqual(get_gcd([12, -15, 18, 21]), 3)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            get_gcd([])
