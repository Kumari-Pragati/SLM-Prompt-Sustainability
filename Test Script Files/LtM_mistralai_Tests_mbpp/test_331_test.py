import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_unset_bits(0), 1)
        self.assertEqual(count_unset_bits(1), 1)
        self.assertEqual(count_unset_bits(3), 2)
        self.assertEqual(count_unset_bits(7), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(count_unset_bits(1 << 31), 32)
        self.assertEqual(count_unset_bits((1 << 31) - 1), 31)
        self.assertEqual(count_unset_bits(0b1000_0000), 1)
        self.assertEqual(count_unset_bits(0b1111_1111), 8)

    def test_complex(self):
        self.assertEqual(count_unset_bits(0b10101010), 5)
        self.assertEqual(count_unset_bits(0b11011011), 4)
        self.assertEqual(count_unset_bits(0b10110110), 5)
