import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_rearrange_bigger_positive(self):
        self.assertEqual(rearrange_bigger(123456), 123456)
        self.assertEqual(rearrange_bigger(561234), 651234)
        self.assertEqual(rearrange_bigger(12345), 12345)
        self.assertEqual(rearrange_bigger(123), 123)
        self.assertEqual(rearrange_bigger(12), 21)

    def test_rearrange_bigger_zero(self):
        self.assertEqual(rearrange_bigger(0), False)

    def test_rearrange_bigger_negative(self):
        self.assertEqual(rearrange_bigger(-123456), False)

    def test_rearrange_bigger_single_digit(self):
        self.assertEqual(rearrange_bigger(1), 1)
        self.assertEqual(rearrange_bigger(2), 2)
        self.assertEqual(rearrange_bigger(3), 3)
        self.assertEqual(rearrange_bigger(4), 4)
        self.assertEqual(rearrange_bigger(5), 5)
        self.assertEqual(rearrange_bigger(6), 6)
        self.assertEqual(rearrange_bigger(7), 7)
        self.assertEqual(rearrange_bigger(8), 8)
        self.assertEqual(rearrange_bigger(9), 9)
