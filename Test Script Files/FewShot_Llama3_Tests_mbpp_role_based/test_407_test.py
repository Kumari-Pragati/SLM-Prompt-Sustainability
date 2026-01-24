import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rearrange_bigger(123456), 123654)

    def test_edge_case_single_digit(self):
        self.assertEqual(rearrange_bigger(5), 5)

    def test_edge_case_two_digits(self):
        self.assertEqual(rearrange_bigger(12), 12)

    def test_edge_case_three_digits(self):
        self.assertEqual(rearrange_bigger(123), 123)

    def test_edge_case_max_digits(self):
        self.assertEqual(rearrange_bigger(987654321), 987654321)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            rearrange_bigger('abc')

    def test_invalid_input_negative_number(self):
        with self.assertRaises(TypeError):
            rearrange_bigger(-123)
