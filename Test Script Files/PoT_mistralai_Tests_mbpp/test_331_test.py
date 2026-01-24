import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_unset_bits(0), 1)
        self.assertEqual(count_unset_bits(1), 1)
        self.assertEqual(count_unset_bits(3), 2)
        self.assertEqual(count_unset_bits(5), 3)
        self.assertEqual(count_unset_bits(7), 3)
        self.assertEqual(count_unset_bits(8), 1)
        self.assertEqual(count_unset_bits(15), 4)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_unset_bits(1 << 31), 32)
        self.assertEqual(count_unset_bits(1 << 63), 64)
        self.assertEqual(count_unset_bits(1 << 127), 128)
        self.assertEqual(count_unset_bits(1 << 64) - 1, 64)
        self.assertEqual(count_unset_bits(1 << 128) - 1, 128)
