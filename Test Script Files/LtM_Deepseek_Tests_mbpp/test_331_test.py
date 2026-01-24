import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_unset_bits(0), 32)
        self.assertEqual(count_unset_bits(1), 31)
        self.assertEqual(count_unset_bits(2), 30)
        self.assertEqual(count_unset_bits(3), 29)

    def test_edge_conditions(self):
        self.assertEqual(count_unset_bits(2**32 - 1), 0)
        self.assertEqual(count_unset_bits(2**32), 32)

    def test_boundary_conditions(self):
        self.assertEqual(count_unset_bits(2**31 - 1), 16)
        self.assertEqual(count_unset_bits(2**31), 16)
        self.assertEqual(count_unset_bits(2**31 + 1), 16)

    def test_complex_cases(self):
        self.assertEqual(count_unset_bits(2**30), 30)
        self.assertEqual(count_unset_bits(2**30 - 1), 31)
        self.assertEqual(count_unset_bits(2**30 + 1), 31)
