import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(toggle_middle_bits(0), 0)
        self.assertEqual(toggle_middle_bits(1), 1)
        self.assertEqual(toggle_middle_bits(2), 3)
        self.assertEqual(toggle_middle_bits(3), 1)
        self.assertEqual(toggle_middle_bits(4), 7)
        self.assertEqual(toggle_middle_bits(5), 5)
        self.assertEqual(toggle_middle_bits(6), 7)
        self.assertEqual(toggle_middle_bits(7), 1)

    def test_edge_cases(self):
        self.assertEqual(toggle_middle_bits(0x80000000), 0x7fffffff)
        self.assertEqual(toggle_middle_bits(0x7fffffff), 0x80000000)
        self.assertEqual(toggle_middle_bits(0x10000000), 0xf0000000)
        self.assertEqual(toggle_middle_bits(0xf0000000), 0x10000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            toggle_middle_bits('a')
        with self.assertRaises(TypeError):
            toggle_middle_bits(None)
