import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Unset_Bits(1), 1)
        self.assertEqual(count_Unset_Bits(2), 2)
        self.assertEqual(count_Unset_Bits(3), 2)
        self.assertEqual(count_Unset_Bits(4), 4)

    def test_edge_conditions(self):
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(5), 4)
        self.assertEqual(count_Unset_Bits(8), 8)

    def test_boundary_conditions(self):
        self.assertEqual(count_Unset_Bits(1023), 1023)
        self.assertEqual(count_Unset_Bits(1024), 1024)
        self.assertEqual(count_Unset_Bits(2047), 2047)

    def test_complex_cases(self):
        self.assertEqual(count_Unset_Bits(2048), 2048)
        self.assertEqual(count_Unset_Bits(3071), 3071)
        self.assertEqual(count_Unset_Bits(3072), 3072)
