import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(rearrange_bigger(123), 123)
        self.assertEqual(rearrange_bigger(321), 321)
        self.assertEqual(rearrange_bigger(54263), 54623)

    def test_edge_cases(self):
        self.assertEqual(rearrange_bigger(9), False)
        self.assertEqual(rearrange_bigger(10), 10)
        self.assertEqual(rearrange_bigger(99), 99)
        self.assertEqual(rearrange_bigger(100), 99)
        self.assertEqual(rearrange_bigger(999), 999)
        self.assertEqual(rearrange_bigger(1000), 999)

    def test_complex_cases(self):
        self.assertEqual(rearrange_bigger(123456), 123465)
        self.assertEqual(rearrange_bigger(654321), 654312)
        self.assertEqual(rearrange_bigger(1234567), 1234567)
        self.assertEqual(rearrange_bigger(123456789), 123456789)
        self.assertEqual(rearrange_bigger(1234567890), 1234567890)
        self.assertEqual(rearrange_bigger(12345678901), False)
