import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(odd_bit_set_number(10), 28)

    def test_boundary_conditions(self):
        self.assertEqual(odd_bit_set_number(0), 1)
        self.assertEqual(odd_bit_set_number(1), 3)

    def test_edge_conditions(self):
        self.assertEqual(odd_bit_set_number(255), 511)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_bit_set_number('a')
        with self.assertRaises(TypeError):
            odd_bit_set_number(None)
