import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(toggle_middle_bits(0), 1)

    def test_one(self):
        self.assertEqual(toggle_middle_bits(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(toggle_middle_bits(2**i), 1 if i == 1 else 0)

    def test_negative_numbers(self):
        self.assertEqual(toggle_middle_bits(-1), 0)

    def test_large_numbers(self):
        self.assertEqual(toggle_middle_bits(2**31 - 1), 0)
