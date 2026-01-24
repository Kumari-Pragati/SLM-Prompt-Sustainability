import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rearrange_bigger(12345), 52341)
        self.assertEqual(rearrange_bigger(98765), 98765)
        self.assertEqual(rearrange_bigger(112233), 321132)

    def test_edge_cases(self):
        self.assertEqual(rearrange_bigger(10000), 10000)
        self.assertEqual(rearrange_bigger(1234567890), 9876543210)

    def test_boundary_cases(self):
        self.assertEqual(rearrange_bigger(12345678901234567890), 98765432109876543210)
        self.assertEqual(rearrange_bigger(10000000000000000000), False)

    def test_invalid_inputs(self):
        self.assertFalse(rearrange_bigger(-12345))
        self.assertFalse(rearrange_bigger('abcde'))
        self.assertFalse(rearrange_bigger(123456789012345678901))
