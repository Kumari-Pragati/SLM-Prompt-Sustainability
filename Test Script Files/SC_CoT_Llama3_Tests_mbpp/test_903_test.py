import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_Unset_Bits(5), 2)
        self.assertEqual(count_Unset_Bits(8), 3)
        self.assertEqual(count_Unset_Bits(16), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(1), 0)
        self.assertEqual(count_Unset_Bits(2), 1)
        self.assertEqual(count_Unset_Bits(3), 1)
        self.assertEqual(count_Unset_Bits(4), 2)
        self.assertEqual(count_Unset_Bits(5), 2)
        self.assertEqual(count_Unset_Bits(6), 2)
        self.assertEqual(count_Unset_Bits(7), 1)
        self.assertEqual(count_Unset_Bits(8), 3)
        self.assertEqual(count_Unset_Bits(9), 2)
        self.assertEqual(count_Unset_Bits(10), 3)
        self.assertEqual(count_Unset_Bits(11), 2)
        self.assertEqual(count_Unset_Bits(12), 2)
        self.assertEqual(count_Unset_Bits(13), 2)
        self.assertEqual(count_Unset_Bits(14), 3)
        self.assertEqual(count_Unset_Bits(15), 4)
        self.assertEqual(count_Unset_Bits(16), 4)

    def test_special_and_corner_cases(self):
        self.assertEqual(count_Unset_Bits(2**31 - 1), 31)
        self.assertEqual(count_Unset_Bits(2**31), 31)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Unset_Bits('a')
        with self.assertRaises(TypeError):
            count_Unset_Bits(None)
        with self.assertRaises(TypeError):
            count_Unset_Bits([1, 2, 3])
