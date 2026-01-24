import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):
    def test_rearrange_bigger_positive_numbers(self):
        self.assertEqual(rearrange_bigger(12345), 54321)
        self.assertEqual(rearrange_bigger(987654), 654987)
        self.assertEqual(rearrange_bigger(10203040), 40302010)

    def test_rearrange_bigger_zero(self):
        self.assertEqual(rearrange_bigger(0), 0)

    def test_rearrange_bigger_negative_numbers(self):
        self.assertEqual(rearrange_bigger(-12345), -54321)
        self.assertEqual(rearrange_bigger(-987654), -654987)
        self.assertEqual(rearrange_bigger(-10203040), -40302010)

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

    def test_rearrange_bigger_empty_string(self):
        self.assertEqual(rearrange_bigger(""), False)

    def test_rearrange_bigger_invalid_input(self):
        self.assertRaises(TypeError, rearrange_bigger, "not_a_number")
