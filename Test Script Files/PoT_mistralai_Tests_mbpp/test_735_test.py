import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(toggle_middle_bits(0), 1)
        self.assertEqual(toggle_middle_bits(2), 3)
        self.assertEqual(toggle_middle_bits(15), 14)
        self.assertEqual(toggle_middle_bits(255), 254)
        self.assertEqual(toggle_middle_bits(65281), 65280)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(toggle_middle_bits(1), 1)
        self.assertEqual(toggle_middle_bits(0), 1)
        self.assertEqual(toggle_middle_bits(2 ** 16 - 1), 2 ** 16 - 1)
        self.assertEqual(toggle_middle_bits(2 ** 32 - 1), 2 ** 32 - 1)
