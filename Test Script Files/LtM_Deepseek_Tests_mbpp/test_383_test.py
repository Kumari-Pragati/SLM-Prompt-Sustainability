import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 2)
        self.assertEqual(even_bit_toggle_number(2), 1)
        self.assertEqual(even_bit_toggle_number(3), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_bit_toggle_number(1023), 1023)
        self.assertEqual(even_bit_toggle_number(1024), 0)
        self.assertEqual(even_bit_toggle_number(1025), 2)
        self.assertEqual(even_bit_toggle_number(2048), 1024)

    def test_more_complex_cases(self):
        self.assertEqual(even_bit_toggle_number(4095), 4095)
        self.assertEqual(even_bit_toggle_number(4096), 2048)
        self.assertEqual(even_bit_toggle_number(8191), 8191)
        self.assertEqual(even_bit_toggle_number(8192), 4096)
