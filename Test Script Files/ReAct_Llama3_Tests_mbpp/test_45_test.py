import unittest
from mbpp_45_code import get_gcd

class TestGetGcd(unittest.TestCase):
    def test_single_pair(self):
        self.assertEqual(get_gcd([1, 2]), 1)

    def test_multiple_pairs(self):
        self.assertEqual(get_gcd([2, 3, 4, 6]), 2)

    def test_single_element(self):
        with self.assertRaises(IndexError):
            get_gcd([1])

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            get_gcd([])

    def test_single_element_list(self):
        self.assertEqual(get_gcd([5]), 5)

    def test_multiple_elements(self):
        self.assertEqual(get_gcd([12, 15, 18, 21, 24, 30]), 3)
