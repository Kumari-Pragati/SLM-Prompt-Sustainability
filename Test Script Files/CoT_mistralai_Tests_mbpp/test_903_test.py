import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(1), 0)
        self.assertEqual(count_Unset_Bits(2), 1)
        self.assertEqual(count_Unset_Bits(3), 1)
        self.assertEqual(count_Unset_Bits(4), 2)
        self.assertEqual(count_Unset_Bits(5), 2)
        self.assertEqual(count_Unset_Bits(6), 3)
        self.assertEqual(count_Unset_Bits(7), 3)
        self.assertEqual(count_Unset_Bits(8), 4)
        self.assertEqual(count_Unset_Bits(9), 4)
        self.assertEqual(count_Unset_Bits(10), 5)
        self.assertEqual(count_Unset_Bits(11), 5)
        self.assertEqual(count_Unset_Bits(12), 6)
        self.assertEqual(count_Unset_Bits(13), 6)
        self.assertEqual(count_Unset_Bits(14), 7)
        self.assertEqual(count_Unset_Bits(15), 7)
        self.assertEqual(count_Unset_Bits(16), 8)
        self.assertEqual(count_Unset_Bits(17), 8)
        self.assertEqual(count_Unset_Bits(18), 9)
        self.assertEqual(count_Unset_Bits(19), 9)
        self.assertEqual(count_Unset_Bits(20), 10)
        self.assertEqual(count_Unset_Bits(21), 10)
        self.assertEqual(count_Unset_Bits(22), 11)
        self.assertEqual(count_Unset_Bits(23), 11)
        self.assertEqual(count_Unset_Bits(24), 12)
        self.assertEqual(count_Unset_Bits(25), 12)
        self.assertEqual(count_Unset_Bits(26), 13)
        self.assertEqual(count_Unset_Bits(27), 13)
        self.assertEqual(count_Unset_Bits(28), 14)
        self.assertEqual(count_Unset_Bits(29), 14)
        self.assertEqual(count_Unset_Bits(30), 15)
        self.assertEqual(count_Unset_Bits(31), 15)

    def test_edge_cases(self):
        self.assertEqual(count_Unset_Bits(-1), 32)
        self.assertEqual(count_Unset_Bits(32), 32)
        self.assertEqual(count_Unset_Bits(2**31), 31)
        self.assertEqual(count_Unset_Bits(2**32 - 1), 32)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, count_Unset_Bits, -2)
        self.assertRaises(ValueError, count_Unset_Bits, float('inf'))
        self.assertRaises(ValueError, count_Unset_Bits, complex(0, 0))
