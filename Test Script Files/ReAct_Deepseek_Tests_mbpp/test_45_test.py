import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_gcd([48, 18]), 6)

    def test_typical_case_with_larger_numbers(self):
        self.assertEqual(get_gcd([101, 103, 107]), 1)

    def test_typical_case_with_negative_numbers(self):
        self.assertEqual(get_gcd([-48, -18]), 6)

    def test_typical_case_with_mixed_positive_and_negative_numbers(self):
        self.assertEqual(get_gcd([-48, 18]), 6)

    def test_edge_case_with_zero(self):
        self.assertEqual(get_gcd([0, 18]), 18)
        self.assertEqual(get_gcd([48, 0]), 48)

    def test_edge_case_with_single_number(self):
        self.assertEqual(get_gcd([48]), 48)

    def test_error_case_with_empty_list(self):
        with self.assertRaises(IndexError):
            get_gcd([])

    def test_error_case_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            get_gcd([48, '18'])
