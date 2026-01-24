import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):
    def test_toggle_middle_bits_positive_numbers(self):
        self.assertEqual(toggle_middle_bits(0b10101010), 0b10101011)

    def test_toggle_middle_bits_negative_numbers(self):
        self.assertEqual(toggle_middle_bits(-0b10101010), -0b10101011)

    def test_toggle_middle_bits_zero(self):
        self.assertEqual(toggle_middle_bits(0), 0)

    def test_toggle_middle_bits_one(self):
        self.assertEqual(toggle_middle_bits(1), 1)

    def test_toggle_middle_bits_max_value(self):
        self.assertEqual(toggle_middle_bits(0b11111111), 0b11111110)

    def test_toggle_middle_bits_min_value(self):
        self.assertEqual(toggle_middle_bits(-0b11111111), -0b11111110)
