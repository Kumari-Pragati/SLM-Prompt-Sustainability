import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_bit_set_number(10), 14)

    def test_boundary_conditions(self):
        self.assertEqual(even_bit_set_number(0), 0)
        self.assertEqual(even_bit_set_number(1), 1)

    def test_edge_cases(self):
        self.assertEqual(even_bit_set_number(2), 2)
        self.assertEqual(even_bit_set_number(3), 7)
        self.assertEqual(even_bit_set_number(4), 4)
        self.assertEqual(even_bit_set_number(5), 15)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_bit_set_number('a')
        with self.assertRaises(TypeError):
            even_bit_set_number(None)
        with self.assertRaises(TypeError):
            even_bit_set_number([])
        with self.assertRaises(TypeError):
            even_bit_set_number({})
