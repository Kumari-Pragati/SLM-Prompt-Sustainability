import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(count_unset_bits(0), 0)
        self.assertEqual(count_unset_bits(1), 1)
        self.assertEqual(count_unset_bits(2), 1)
        self.assertEqual(count_unset_bits(3), 0)
        self.assertEqual(count_unset_bits(4), 2)
        self.assertEqual(count_unset_bits(5), 1)
        self.assertEqual(count_unset_bits(6), 2)
        self.assertEqual(count_unset_bits(7), 0)
        self.assertEqual(count_unset_bits(8), 3)
        self.assertEqual(count_unset_bits(9), 2)
        self.assertEqual(count_unset_bits(10), 3)
        self.assertEqual(count_unset_bits(11), 2)
        self.assertEqual(count_unset_bits(12), 3)
        self.assertEqual(count_unset_bits(13), 2)
        self.assertEqual(count_unset_bits(14), 3)
        self.assertEqual(count_unset_bits(15), 0)

    def test_edge_cases(self):
        self.assertEqual(count_unset_bits(2**31 - 1), 31)
        self.assertEqual(count_unset_bits(2**31), 32)
        self.assertEqual(count_unset_bits(2**32 - 1), 32)
        self.assertEqual(count_unset_bits(2**32), 33)

    def test_boundary_cases(self):
        self.assertEqual(count_unset_bits(2**31), 32)
        self.assertEqual(count_unset_bits(2**32 - 1), 32)
        self.assertEqual(count_unset_bits(2**32), 33)
