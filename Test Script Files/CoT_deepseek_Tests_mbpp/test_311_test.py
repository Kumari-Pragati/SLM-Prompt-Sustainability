import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(set_left_most_unset_bit(10), 12)

    def test_edge_case_already_set(self):
        self.assertEqual(set_left_most_unset_bit(15), 15)

    def test_edge_case_zero(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)

    def test_boundary_case_max_int(self):
        self.assertEqual(set_left_most_unset_bit(2147483647), 2147483648)

    def test_invalid_input_negative(self):
        with self.assertRaises(Exception):
            set_left_most_unset_bit(-10)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(Exception):
            set_left_most_unset_bit("10")
