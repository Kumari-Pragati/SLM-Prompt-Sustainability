import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(number_ctr("hello123"), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(number_ctr(""), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(number_ctr("1"), 1)

    def test_edge_case_single_non_digit(self):
        self.assertEqual(number_ctr("a"), 0)

    def test_edge_case_all_digits(self):
        self.assertEqual(number_ctr("1234567890"), 10)

    def test_edge_case_mixed_digits_and_non_digits(self):
        self.assertEqual(number_ctr("hello123abc"), 3)

    def test_edge_case_multiple_non_digits(self):
        self.assertEqual(number_ctr("abc123def"), 2)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            number_ctr(123)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            number_ctr([])
