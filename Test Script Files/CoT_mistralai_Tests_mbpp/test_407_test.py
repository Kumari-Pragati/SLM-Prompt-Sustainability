import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):
    def test_rearrange_bigger_positive(self):
        self.assertEqual(rearrange_bigger(123456), 123456)
        self.assertEqual(rearrange_bigger(561234), 561234)
        self.assertEqual(rearrange_bigger(123465), 123465)
        self.assertEqual(rearrange_bigger(123405), 123405)
        self.assertEqual(rearrange_bigger(120345), 120345)

    def test_rearrange_bigger_negative(self):
        self.assertNotEqual(rearrange_bigger(12345), False)
        self.assertNotEqual(rearrange_bigger(1234), False)
        self.assertNotEqual(rearrange_bigger(123), False)
        self.assertNotEqual(rearrange_bigger(12), False)
        self.assertNotEqual(rearrange_bigger(1), False)

    def test_rearrange_bigger_edge_cases(self):
        self.assertEqual(rearrange_bigger(10), 10)
        self.assertEqual(rearrange_bigger(9), 9)
        self.assertEqual(rearrange_bigger(11), 11)
        self.assertEqual(rearrange_bigger(0), 0)
        self.assertEqual(rearrange_bigger(99), 99)
        self.assertEqual(rearrange_bigger(100), 100)

    def test_rearrange_bigger_invalid_inputs(self):
        self.assertRaises(ValueError, rearrange_bigger, -1)
        self.assertRaises(ValueError, rearrange_bigger, "string")
