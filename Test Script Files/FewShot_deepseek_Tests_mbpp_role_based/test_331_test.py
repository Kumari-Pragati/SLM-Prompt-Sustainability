import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_unset_bits(10), 2)

    def test_boundary_conditions(self):
        self.assertEqual(count_unset_bits(0), 1)
        self.assertEqual(count_unset_bits(1), 0)

    def test_edge_conditions(self):
        self.assertEqual(count_unset_bits(2**31 - 1), 31)
        self.assertEqual(count_unset_bits(2**31), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_unset_bits('10')
        with self.assertRaises(TypeError):
            count_unset_bits(10.5)
        with self.assertRaises(TypeError):
            count_unset_bits(None)
