import unittest
from mbpp_545_code import toggle_F_and_L_bits

class TestToggleFAndLBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(toggle_F_and_L_bits(0), 1)
        self.assertEqual(toggle_F_and_L_bits(1), 0)
        self.assertEqual(toggle_F_and_L_bits(3), 2)
        self.assertEqual(toggle_F_and_L_bits(5), 6)
        self.assertEqual(toggle_F_and_L_bits(7), 0)
        self.assertEqual(toggle_F_and_L_bits(15), 14)
        self.assertEqual(toggle_F_and_L_bits(255), 254)
        self.assertEqual(toggle_F_and_L_bits(256), 0)
        self.assertEqual(toggle_F_and_L_bits(65281), 65280)
        self.assertEqual(toggle_F_and_L_bits(65535), 65534)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(toggle_F_and_L_bits(0b00000000), 1)
        self.assertEqual(toggle_F_and_L_bits(0b00000001), 0)
        self.assertEqual(toggle_F_and_L_bits(0b00000010), 9)
        self.assertEqual(toggle_F_and_L_bits(0b00000011), 2)
        self.assertEqual(toggle_F_and_L_bits(0b00001111), 15)
        self.assertEqual(toggle_F_and_L_bits(0b00011111), 28)
        self.assertEqual(toggle_F_and_L_bits(0b01111111), 127)
        self.assertEqual(toggle_F_and_L_bits(0b10000000), 128)
        self.assertEqual(toggle_F_and_L_bits(0b11111111), 255)
        self.assertEqual(toggle_F_and_L_bits(0b100000000), 256)
        self.assertEqual(toggle_F_and_L_bits(0b1111111111111111), 16777215)
        self.assertEqual(toggle_F_and_L_bits(0b11111111111111111111), 16777214)
