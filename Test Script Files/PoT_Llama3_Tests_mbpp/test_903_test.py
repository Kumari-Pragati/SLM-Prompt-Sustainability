import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Unset_Bits(5), 2)

    def test_edge_case(self):
        self.assertEqual(count_Unset_Bits(1), 0)
        self.assertEqual(count_Unset_Bits(2), 1)
        self.assertEqual(count_Unset_Bits(3), 1)
        self.assertEqual(count_Unset_Bits(4), 2)

    def test_boundary_case(self):
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(8), 3)

    def test_corner_case(self):
        self.assertEqual(count_Unset_Bits(15), 4)
