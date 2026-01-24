import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(toggle_middle_bits(0), 0)
        self.assertEqual(toggle_middle_bits(1), 1)
        self.assertEqual(toggle_middle_bits(2), 3)
        self.assertEqual(toggle_middle_bits(3), 2)
        self.assertEqual(toggle_middle_bits(4), 5)
        self.assertEqual(toggle_middle_bits(5), 4)
        self.assertEqual(toggle_middle_bits(6), 7)
        self.assertEqual(toggle_middle_bits(7), 6)
        self.assertEqual(toggle_middle_bits(8), 9)
        self.assertEqual(toggle_middle_bits(9), 8)

    def test_edge_cases(self):
        self.assertEqual(toggle_middle_bits(1023), 1022)
        self.assertEqual(toggle_middle_bits(1024), 1025)
        self.assertEqual(toggle_middle_bits(2047), 2046)
        self.assertEqual(toggle_middle_bits(2048), 2049)

    def test_boundary_cases(self):
        self.assertEqual(toggle_middle_bits(1024), 1025)
        self.assertEqual(toggle_middle_bits(2048), 2049)
        self.assertEqual(toggle_middle_bits(4095), 4094)
        self.assertEqual(toggle_middle_bits(4096), 4097)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            toggle_middle_bits("invalid")
