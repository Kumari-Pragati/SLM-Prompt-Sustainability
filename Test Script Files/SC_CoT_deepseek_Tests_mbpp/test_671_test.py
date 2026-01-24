import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0b10100), 0b10110)
        self.assertEqual(set_Right_most_Unset_Bit(0b11000), 0b11001)
        self.assertEqual(set_Right_most_Unset_Bit(0b11111), 0b11111)

    def test_edge_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)
        self.assertEqual(set_Right_most_Unset_Bit(0b11111111), 0b11111111)

    def test_corner_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0b1000), 0b1001)
        self.assertEqual(set_Right_most_Unset_Bit(0b100000), 0b100001)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            set_Right_most_Unset_Bit('invalid')
        with self.assertRaises(TypeError):
            set_Right_most_Unset_Bit(None)
