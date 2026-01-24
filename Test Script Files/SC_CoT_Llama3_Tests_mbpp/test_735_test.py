import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):
    def test_toggle_middle_bits_normal(self):
        self.assertEqual(toggle_middle_bits(0), 0)
        self.assertEqual(toggle_middle_bits(1), 1)
        self.assertEqual(toggle_middle_bits(2), 3)
        self.assertEqual(toggle_middle_bits(3), 3)
        self.assertEqual(toggle_middle_bits(4), 0)
        self.assertEqual(toggle_middle_bits(5), 5)
        self.assertEqual(toggle_middle_bits(6), 7)
        self.assertEqual(toggle_middle_bits(7), 7)
        self.assertEqual(toggle_middle_bits(8), 0)
        self.assertEqual(toggle_middle_bits(15), 15)

    def test_toggle_middle_bits_edge(self):
        self.assertEqual(toggle_middle_bits(0x00000001), 0x00000001)
        self.assertEqual(toggle_middle_bits(0x00000002), 0x00000003)
        self.assertEqual(toggle_middle_bits(0x00000004), 0x00000000)
        self.assertEqual(toggle_middle_bits(0x00000008), 0x00000008)
        self.assertEqual(toggle_middle_bits(0x00000010), 0x00000000)
        self.assertEqual(toggle_middle_bits(0x00000020), 0x00000040)
        self.assertEqual(toggle_middle_bits(0x00000040), 0x00000040)
        self.assertEqual(toggle_middle_bits(0x00000080), 0x00000080)
        self.assertEqual(toggle_middle_bits(0x00000100), 0x00000000)
        self.assertEqual(toggle_middle_bits(0x00010000), 0x00010000)

    def test_toggle_middle_bits_special(self):
        self.assertEqual(toggle_middle_bits(0x00000003), 0x00000003)
        self.assertEqual(toggle_middle_bits(0x00000005), 0x00000005)
        self.assertEqual(toggle_middle_bits(0x00000007), 0x00000007)
        self.assertEqual(toggle_middle_bits(0x0000000f), 0x0000000f)
        self.assertEqual(toggle_middle_bits(0x0000001f), 0x0000001f)
        self.assertEqual(toggle_middle_bits(0x0000003f), 0x0000003f)
        self.assertEqual(toggle_middle_bits(0x0000007f), 0x0000007f)
        self.assertEqual(toggle_middle_bits(0x000000ff), 0x000000ff)
        self.assertEqual(toggle_middle_bits(0x0000ffff), 0x0000ffff)

    def test_toggle_middle_bits_invalid(self):
        with self.assertRaises(TypeError):
            toggle_middle_bits('a')
        with self.assertRaises(TypeError):
            toggle_middle_bits(None)
