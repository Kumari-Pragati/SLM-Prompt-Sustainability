import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(toggle_middle_bits(0), 1)

    def test_one(self):
        self.assertEqual(toggle_middle_bits(1), 1)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(toggle_middle_bits(1 << i), 1 << (i - 1))

    def test_negative_numbers(self):
        self.assertEqual(toggle_middle_bits(-1), 0)
        self.assertEqual(toggle_middle_bits(-2), 1)

    def test_large_numbers(self):
        max_int = (1 << 31) - 1
        self.assertEqual(toggle_middle_bits(max_int), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            toggle_middle_bits(3.14)
        with self.assertRaises(TypeError):
            toggle_middle_bits('str')
