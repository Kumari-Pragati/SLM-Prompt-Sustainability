import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(count_Unset_Bits(5), 3)

    def test_boundary_conditions(self):
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(1), 0)
        self.assertEqual(count_Unset_Bits(2), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Unset_Bits(3), 2)
        self.assertEqual(count_Unset_Bits(4), 1)
        self.assertEqual(count_Unset_Bits(8), 4)

    def test_large_number(self):
        self.assertEqual(count_Unset_Bits(1000), 400)
