import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2), 3)
        self.assertEqual(odd_bit_set_number(4), 5)
        self.assertEqual(odd_bit_set_number(7), 7)

    def test_edge_and_boundary(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(8), 9)
        self.assertEqual(odd_bit_set_number(16), 17)
        self.assertEqual(odd_bit_set_number(32), 33)
        self.assertEqual(odd_bit_set_number(64), 65)
        self.assertEqual(odd_bit_set_number(128), 129)

    def test_complex(self):
        self.assertEqual(odd_bit_set_number(1025), 1027)
        self.assertEqual(odd_bit_set_number(2049), 2051)
        self.assertEqual(odd_bit_set_number(4097), 4099)
        self.assertEqual(odd_bit_set_number(8193), 8195)
        self.assertEqual(odd_bit_set_number(16385), 16387)
        self.assertEqual(odd_bit_set_number(32769), 32771)
        self.assertEqual(odd_bit_set_number(65537), 65539)
        self.assertEqual(odd_bit_set_number(131073), 131075)
