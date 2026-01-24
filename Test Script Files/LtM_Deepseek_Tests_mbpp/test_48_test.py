import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(1), 3)
        self.assertEqual(odd_bit_set_number(2), 5)
        self.assertEqual(odd_bit_set_number(3), 7)

    def test_edge_conditions(self):
        self.assertEqual(odd_bit_set_number(1023), 1047)
        self.assertEqual(odd_bit_set_number(2047), 2079)

    def test_boundary_conditions(self):
        self.assertEqual(odd_bit_set_number(2**31 - 1), 2**31)
        self.assertEqual(odd_bit_set_number(2**63 - 1), 2**63)

    def test_complex_cases(self):
        self.assertEqual(odd_bit_set_number(10000000000), 10000000014)
        self.assertEqual(odd_bit_set_number(10000000000000), 10000000000014)
