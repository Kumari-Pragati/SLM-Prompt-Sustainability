import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):

    def test_toggle_middle_bits_typical_cases(self):
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

    def test_toggle_middle_bits_edge_cases(self):
        self.assertEqual(toggle_middle_bits(10), 11)
        self.assertEqual(toggle_middle_bits(11), 10)
        self.assertEqual(toggle_middle_bits(12), 13)
        self.assertEqual(toggle_middle_bits(13), 12)
        self.assertEqual(toggle_middle_bits(14), 15)
        self.assertEqual(toggle_middle_bits(15), 14)
        self.assertEqual(toggle_middle_bits(16), 17)
        self.assertEqual(toggle_middle_bits(17), 16)
        self.assertEqual(toggle_middle_bits(18), 19)
        self.assertEqual(toggle_middle_bits(19), 18)

    def test_toggle_middle_bits_error_cases(self):
        with self.assertRaises(TypeError):
            toggle_middle_bits('a')
        with self.assertRaises(TypeError):
            toggle_middle_bits(None)
        with self.assertRaises(TypeError):
            toggle_middle_bits(float('nan'))
