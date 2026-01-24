import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_Digits(10), 2)

    def test_edge_case_negative(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_edge_case_zero(self):
        self.assertEqual(find_Digits(0), 1)

    def test_edge_case_one(self):
        self.assertEqual(find_Digits(1), 1)

    def test_edge_case_large_number(self):
        self.assertEqual(find_Digits(1000), 4)

    def test_edge_case_large_number_with_decimal(self):
        self.assertEqual(find_Digits(1000.5), 4)

    def test_edge_case_zero_with_decimal(self):
        self.assertEqual(find_Digits(0.5), 1)

    def test_edge_case_negative_with_decimal(self):
        self.assertEqual(find_Digits(-0.5), 0)

    def test_edge_case_large_negative(self):
        self.assertEqual(find_Digits(-1000), 0)

    def test_edge_case_large_positive(self):
        self.assertEqual(find_Digits(1000), 4)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Digits('a')
