import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):

    def test_toggle_middle_bits_typical_cases(self):
        self.assertEqual(toggle_middle_bits(0b10101010), 0b01010101)
        self.assertEqual(toggle_middle_bits(0b11110000), 0b11111111)
        self.assertEqual(toggle_middle_bits(0b10001000), 0b01110111)

    def test_toggle_middle_bits_edge_cases(self):
        self.assertEqual(toggle_middle_bits(0b1), 1)
        self.assertEqual(toggle_middle_bits(0b0), 0)
        self.assertEqual(toggle_middle_bits(0b11111111), 0b11111111)

    def test_toggle_middle_bits_invalid_inputs(self):
        with self.assertRaises(TypeError):
            toggle_middle_bits("invalid input")
        with self.assertRaises(TypeError):
            toggle_middle_bits(None)
