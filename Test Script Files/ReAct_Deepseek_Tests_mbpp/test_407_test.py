import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rearrange_bigger(12345), 12435)
        self.assertEqual(rearrange_bigger(98765), 98765)
        self.assertEqual(rearrange_bigger(11223), 12123)

    def test_edge_cases(self):
        self.assertEqual(rearrange_bigger(11111), False)
        self.assertEqual(rearrange_bigger(99999), False)
        self.assertEqual(rearrange_bigger(123456), 123546)

    def test_explicitly_handled_error_cases(self):
        self.assertFalse(rearrange_bigger(-12345))
        self.assertFalse(rearrange_bigger(0))
        self.assertFalse(rearrange_bigger(100000))
