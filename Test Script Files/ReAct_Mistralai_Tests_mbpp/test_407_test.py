import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_rearrange_bigger_positive_numbers(self):
        self.assertEqual(rearrange_bigger(1234), 1234)
        self.assertEqual(rearrange_bigger(54321), 54321)
        self.assertEqual(rearrange_bigger(987654321), 987654321)

    def test_rearrange_bigger_negative_numbers(self):
        self.assertEqual(rearrange_bigger(-1234), -1234)
        self.assertEqual(rearrange_bigger(-54321), -54321)
        self.assertEqual(rearrange_bigger(-987654321), -987654321)

    def test_rearrange_bigger_zero(self):
        self.assertEqual(rearrange_bigger(0), 0)

    def test_rearrange_bigger_single_digit(self):
        self.assertEqual(rearrange_bigger(1), 1)
        self.assertEqual(rearrange_bigger(9), 9)

    def test_rearrange_bigger_two_digits(self):
        self.assertEqual(rearrange_bigger(10), 10)
        self.assertEqual(rearrange_bigger(99), 99)

    def test_rearrange_bigger_leading_zeros(self):
        self.assertEqual(rearrange_bigger(00123), 123)
        self.assertEqual(rearrange_bigger(01234), 1234)
        self.assertEqual(rearrange_bigger(09876), 9876)

    def test_rearrange_bigger_edge_cases(self):
        self.assertEqual(rearrange_bigger(123), 123)
        self.assertEqual(rearrange_bigger(1230), 1230)
        self.assertEqual(rearrange_bigger(12300), 12300)
        self.assertEqual(rearrange_bigger(123000), 123000)

    def test_rearrange_bigger_error_cases(self):
        self.assertFalse(rearrange_bigger(None))
        self.assertFalse(rearrange_bigger("abc"))
        self.assertFalse(rearrange_bigger("123a"))
        self.assertFalse(rearrange_bigger(""))
