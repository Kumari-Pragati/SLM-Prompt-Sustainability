import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Unset_Bits(0), 1)
        self.assertEqual(count_Unset_Bits(2), 1)
        self.assertEqual(count_Unset_Bits(4), 2)
        self.assertEqual(count_Unset_Bits(7), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Unset_Bits(1), 0)
        self.assertEqual(count_Unset_Bits(5), 2)
        self.assertEqual(count_Unset_Bits(8), 3)
        self.assertEqual(count_Unset_Bits(16), 4)
        self.assertEqual(count_Unset_Bits(255), 8)
        self.assertEqual(count_Unset_Bits(256), 8)
        self.assertEqual(count_Unset_Bits(257), 7)
        self.assertEqual(count_Unset_Bits(2147483647), 31)
        self.assertEqual(count_Unset_Bits(2147483648), 31)
