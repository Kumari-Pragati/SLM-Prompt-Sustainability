import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(2), 3)
        self.assertEqual(even_bit_toggle_number(3), 2)
        self.assertEqual(even_bit_toggle_number(4), 6)
        self.assertEqual(even_bit_toggle_number(5), 7)
        self.assertEqual(even_bit_toggle_number(6), 13)
        self.assertEqual(even_bit_toggle_number(7), 11)
        self.assertEqual(even_bit_toggle_number(8), 15)
        self.assertEqual(even_bit_toggle_number(9), 19)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_bit_toggle_number(10), 21)
        self.assertEqual(even_bit_toggle_number(127), 131)
        self.assertEqual(even_bit_toggle_number(128), 129)
        self.assertEqual(even_bit_toggle_number(2147483647), 2147483649)
        self.assertEqual(even_bit_toggle_number(2147483648), 2147483649)

    def test_special_cases(self):
        self.assertEqual(even_bit_toggle_number(-1), 0)
        self.assertEqual(even_bit_toggle_number(-2), 3)
        self.assertEqual(even_bit_toggle_number(-3), 2)
        self.assertEqual(even_bit_toggle_number(-4), 6)
        self.assertEqual(even_bit_toggle_number(-5), 7)
        self.assertEqual(even_bit_toggle_number(-6), 13)
        self.assertEqual(even_bit_toggle_number(-7), 11)
        self.assertEqual(even_bit_toggle_number(-8), 15)
        self.assertEqual(even_bit_toggle_number(-9), 19)
