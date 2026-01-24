import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFandLBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(toggle_F_and_L_bits(0), 1)

    def test_one(self):
        self.assertEqual(toggle_F_and_L_bits(1), 0)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(toggle_F_and_L_bits(1 << i), ~(1 << i))

    def test_negative_numbers(self):
        self.assertEqual(toggle_F_and_L_bits(-1), 0)
        self.assertEqual(toggle_F_and_L_bits(-2), 1)

    def test_large_numbers(self):
        self.assertEqual(toggle_F_and_L_bits(2 ** 31), 2 ** 31 - 1)
        self.assertEqual(toggle_F_and_L_bits(2 ** 31 - 1), 0)
