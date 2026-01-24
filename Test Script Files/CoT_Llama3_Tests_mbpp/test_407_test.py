import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):
    def test_rearrange_bigger(self):
        self.assertEqual(rearrange_bigger(12345), 54321)
        self.assertEqual(rearrange_bigger(123456), 654321)
        self.assertEqual(rearrange_bigger(1234567), 7654321)
        self.assertEqual(rearrange_bigger(12345678), 87654321)
        self.assertFalse(rearrange_bigger(123))
        self.assertFalse(rearrange_bigger(1234567890))
        self.assertFalse(rearrange_bigger(0))
        self.assertFalse(rearrange_bigger(-123456))
