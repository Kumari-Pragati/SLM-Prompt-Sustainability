import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(rearrange_bigger(12345), 12345)
        self.assertEqual(rearrange_bigger(54321), 54321)
        self.assertEqual(rearrange_bigger(123), 123)
        self.assertEqual(rearrange_bigger(321), 321)

    def test_edge_case_single_digit(self):
        self.assertEqual(rearrange_bigger(9), False)
        self.assertEqual(rearrange_bigger(0), False)

    def test_edge_case_two_digits(self):
        self.assertEqual(rearrange_bigger(10), 10)
        self.assertEqual(rearrange_bigger(99), 99)

    def test_edge_case_longer_numbers(self):
        self.assertEqual(rearrange_bigger(100000), 100000)
        self.assertEqual(rearrange_bigger(999999), 999999)

    def test_edge_case_reverse_order(self):
        self.assertEqual(rearrange_bigger(51234), 51432)
        self.assertEqual(rearrange_bigger(543210), 54321)

    def test_invalid_input(self):
        self.assertFalse(rearrange_bigger('abc'))
        self.assertFalse(rearrange_bigger(-123))
        self.assertFalse(rearrange_bigger(123.45))
        self.assertFalse(rearrange_bigger([1, 2, 3]))
