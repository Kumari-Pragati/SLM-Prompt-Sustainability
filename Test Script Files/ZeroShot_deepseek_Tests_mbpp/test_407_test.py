import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_rearrange_bigger(self):
        self.assertEqual(rearrange_bigger(123456), 654321)
        self.assertEqual(rearrange_bigger(987654), 987654)
        self.assertEqual(rearrange_bigger(111111), 111111)
        self.assertEqual(rearrange_bigger(12345), False)
        self.assertEqual(rearrange_bigger(98765), 98765)
        self.assertEqual(rearrange_bigger(123456789), 987654321)
        self.assertEqual(rearrange_bigger(1000000001), 1100000000)
        self.assertEqual(rearrange_bigger(1000000000), False)
