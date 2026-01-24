import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_unset_bits(5), 3)
        self.assertEqual(count_unset_bits(10), 4)
        self.assertEqual(count_unset_bits(21), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_unset_bits(0), 1)
        self.assertEqual(count_unset_bits(1), 1)
        self.assertEqual(count_unset_bits(2**31 - 1), 31)
        self.assertEqual(count_unset_bits(2**32 - 1), 0)

    def test_special_cases(self):
        self.assertEqual(count_unset_bits(3), 2)
        self.assertEqual(count_unset_bits(7), 3)
        self.assertEqual(count_unset_bits(15), 4)
