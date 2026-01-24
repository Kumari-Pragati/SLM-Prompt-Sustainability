import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rearrange_bigger(12345), 12345)
        self.assertEqual(rearrange_bigger(54321), 54321)
        self.assertEqual(rearrange_bigger(123), 123)
        self.assertEqual(rearrange_bigger(321), False)

    def test_edge_cases(self):
        self.assertEqual(rearrange_bigger(0), False)
        self.assertEqual(rearrange_bigger(987654321), 987654321)
        self.assertEqual(rearrange_bigger(102030405), 102030405)
        self.assertEqual(rearrange_bigger(9), False)

    def test_boundary_cases(self):
        self.assertEqual(rearrange_bigger(10), 10)
        self.assertEqual(rearrange_bigger(99), 99)
        self.assertEqual(rearrange_bigger(100), False)
        self.assertEqual(rearrange_bigger(999), 999)
