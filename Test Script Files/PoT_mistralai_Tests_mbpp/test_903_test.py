import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Unset_Bits(0), 32)
        self.assertEqual(count_Unset_Bits(1), 0)
        self.assertEqual(count_Unset_Bits(3), 2)
        self.assertEqual(count_Unset_Bits(4), 1)
        self.assertEqual(count_Unset_Bits(5), 1)
        self.assertEqual(count_Unset_Bits(6), 0)
        self.assertEqual(count_Unset_Bits(7), 3)
        self.assertEqual(count_Unset_Bits(8), 1)
        self.assertEqual(count_Unset_Bits(15), 4)
        self.assertEqual(count_Unset_Bits(16), 0)
        self.assertEqual(count_Unset_Bits(255), 8)
        self.assertEqual(count_Unset_Bits(256), 0)
        self.assertEqual(count_Unset_Bits(511), 9)
        self.assertEqual(count_Unset_Bits(512), 0)
        self.assertEqual(count_Unset_Bits(1023), 10)
        self.assertEqual(count_Unset_Bits(1024), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Unset_Bits(-1), -1)
        self.assertEqual(count_Unset_Bits(2 ** 31), 31)
        self.assertEqual(count_Unset_Bits(2 ** 32 - 1), 32)
        self.assertEqual(count_Unset_Bits(2 ** 64 - 1), 64)
