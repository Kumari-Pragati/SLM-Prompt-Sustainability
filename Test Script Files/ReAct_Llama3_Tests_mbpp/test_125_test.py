import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_length("010101", 10), 2)

    def test_edge_case_zero(self):
        self.assertEqual(find_length("000000", 6), 0)

    def test_edge_case_all_ones(self):
        self.assertEqual(find_length("111111", 6), 6)

    def test_edge_case_all_zeros(self):
        self.assertEqual(find_length("000000", 6), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(find_length("0", 1), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(find_length("", 0), 0)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            find_length(None, 5)

    def test_edge_case_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_length("abc", None)
