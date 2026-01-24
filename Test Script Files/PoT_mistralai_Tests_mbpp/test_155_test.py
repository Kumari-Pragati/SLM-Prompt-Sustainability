import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):

    def test_typical_cases(self):
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
        self.assertEqual(even_bit_toggle_number(10), 27)
        self.assertEqual(even_bit_toggle_number(11), 31)
        self.assertEqual(even_bit_toggle_number(12), 43)
        self.assertEqual(even_bit_toggle_number(13), 47)
        self.assertEqual(even_bit_toggle_number(14), 63)
        self.assertEqual(even_bit_toggle_number(15), 71)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(even_bit_toggle_number(-1), 0)
        self.assertEqual(even_bit_toggle_number(2**31 - 1), 2**31 - 1)
        self.assertEqual(even_bit_toggle_number(2**31), 2**31 - 1)
        self.assertEqual(even_bit_toggle_number(0b1000_0000), 0b1111_1111)
        self.assertEqual(even_bit_toggle_number(0b1111_1111), 0b1000_0000)
