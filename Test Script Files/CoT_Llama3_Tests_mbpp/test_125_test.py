import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_length("110100", 6), 2)

    def test_edge_case_zero(self):
        self.assertEqual(find_length("000000", 6), 0)

    def test_edge_case_all_ones(self):
        self.assertEqual(find_length("111111", 6), 0)

    def test_edge_case_all_zeros(self):
        self.assertEqual(find_length("000000", 6), 0)

    def test_edge_case_single_zero(self):
        self.assertEqual(find_length("100000", 6), 1)

    def test_edge_case_single_one(self):
        self.assertEqual(find_length("010000", 6), 1)

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(find_length("000111", 6), 2)

    def test_edge_case_multiple_ones(self):
        self.assertEqual(find_length("111000", 6), 2)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            find_length(123, 6)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            find_length("123", "six")
