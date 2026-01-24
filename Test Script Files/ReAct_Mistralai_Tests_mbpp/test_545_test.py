import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(toggle_F_and_L_bits(0), 1)

    def test_one(self):
        self.assertEqual(toggle_F_and_L_bits(1), 0)

    def test_powers_of_two(self):
        for i in range(1, 32):
            self.assertEqual(toggle_F_and_L_bits(1 << i), ~(1 << i))

    def test_combinations(self):
        test_cases = [
            (1, 0), (3, 2), (5, 6), (7, 9), (15, 14), (255, 254)
        ]
        for n, expected in test_cases:
            self.assertEqual(toggle_F_and_L_bits(n), expected)

    def test_negative_numbers(self):
        self.assertEqual(toggle_F_and_L_bits(-1), 0)
        self.assertEqual(toggle_F_and_L_bits(-3), 2)
        self.assertEqual(toggle_F_and_L_bits(-5), 6)
        self.assertEqual(toggle_F_and_L_bits(-7), 9)
        self.assertEqual(toggle_F_and_L_bits(-15), 14)
        self.assertEqual(toggle_F_and_L_bits(-255), 254)
