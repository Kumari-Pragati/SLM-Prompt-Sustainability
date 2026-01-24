import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_bit_set_number(10), 14)

    def test_boundary_case(self):
        self.assertEqual(odd_bit_set_number(0), 0)

    def test_edge_case(self):
        self.assertEqual(odd_bit_set_number(1), 1)
        self.assertEqual(odd_bit_set_number(2), 3)
        self.assertEqual(odd_bit_set_number(3), 3)
        self.assertEqual(odd_bit_set_number(4), 7)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_bit_set_number('10')
        with self.assertRaises(TypeError):
            odd_bit_set_number(None)
        with self.assertRaises(TypeError):
            odd_bit_set_number([10])
