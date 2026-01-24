import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Unset_Bits(5), 2)

    def test_boundary_conditions(self):
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(1), 1)
        self.assertEqual(count_Unset_Bits(2), 1)

    def test_edge_conditions(self):
        self.assertEqual(count_Unset_Bits(3), 2)
        self.assertEqual(count_Unset_Bits(4), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Unset_Bits('5')
        with self.assertRaises(ValueError):
            count_Unset_Bits(-5)
