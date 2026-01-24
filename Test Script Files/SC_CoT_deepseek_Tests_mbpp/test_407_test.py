import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearrange_bigger(12345), 52341)

    def test_edge_case(self):
        self.assertEqual(rearrange_bigger(987654321), 987654321)
        self.assertEqual(rearrange_bigger(11111), 11111)

    def test_corner_case(self):
        self.assertEqual(rearrange_bigger(10000), 10000)
        self.assertEqual(rearrange_bigger(99999), 99999)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rearrange_bigger('12345')
        with self.assertRaises(ValueError):
            rearrange_bigger(-12345)
