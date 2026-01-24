import unittest
from mbpp_349_code import check

class TestCheck(unittest.TestCase):
    def test_typical_use_case_yes(self):
        self.assertEqual(check("101"), "Yes")

    def test_typical_use_case_no(self):
        self.assertEqual(check("abc"), "No")

    def test_edge_case_all_zeros(self):
        self.assertEqual(check("000"), "Yes")

    def test_edge_case_all_ones(self):
        self.assertEqual(check("111"), "Yes")

    def test_edge_case_mixed_zeros_and_ones(self):
        self.assertEqual(check("010"), "Yes")

    def test_edge_case_empty_string(self):
        self.assertEqual(check(""), "No")

    def test_edge_case_single_digit(self):
        self.assertEqual(check("0"), "Yes")

    def test_edge_case_single_digit_one(self):
        self.assertEqual(check("1"), "Yes")

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            check(123)
