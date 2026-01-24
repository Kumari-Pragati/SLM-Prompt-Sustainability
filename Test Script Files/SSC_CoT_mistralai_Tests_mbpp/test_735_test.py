import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(toggle_middle_bits(0), 1)
        self.assertEqual(toggle_middle_bits(1), 0)
        self.assertEqual(toggle_middle_bits(2), 3)
        self.assertEqual(toggle_middle_bits(3), 0)
        self.assertEqual(toggle_middle_bits(4), 6)
        self.assertEqual(toggle_middle_bits(5), 7)
        self.assertEqual(toggle_middle_bits(6), 13)
        self.assertEqual(toggle_middle_bits(7), 3)
        self.assertEqual(toggle_middle_bits(8), 15)
        self.assertEqual(toggle_middle_bits(9), 14)
        self.assertEqual(toggle_middle_bits(10), 21)
        self.assertEqual(toggle_middle_bits(11), 23)
        self.assertEqual(toggle_middle_bits(12), 31)
        self.assertEqual(toggle_middle_bits(13), 15)
        self.assertEqual(toggle_middle_bits(14), 27)
        self.assertEqual(toggle_middle_bits(15), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(toggle_middle_bits(0b1000_0000), 0b1111_1111)
        self.assertEqual(toggle_middle_bits(0b1111_1111), 0b1000_0000)
        self.assertEqual(toggle_middle_bits(0b0000_0001), 0b0000_0001)
        self.assertEqual(toggle_middle_bits(0b1111_1110), 0b1111_1101)
        self.assertEqual(toggle_middle_bits(0b1000000000), 0b0111111111)
        self.assertEqual(toggle_middle_bits(0b1111111111), 0b1000000000)
