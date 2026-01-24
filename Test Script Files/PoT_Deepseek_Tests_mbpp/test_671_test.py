import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)
        self.assertEqual(set_Right_most_Unset_Bit(1), 2)
        self.assertEqual(set_Right_most_Unset_Bit(3), 2)
        self.assertEqual(set_Right_most_Unset_Bit(7), 4)
        self.assertEqual(set_Right_most_Unset_Bit(15), 8)

    def test_edge_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(1023), 1024)
        self.assertEqual(set_Right_most_Unset_Bit(2047), 2048)
        self.assertEqual(set_Right_most_Unset_Bit(4095), 4096)

    def test_boundary_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(pow(2, 31) - 1), pow(2, 31))
        self.assertEqual(set_Right_most_Unset_Bit(pow(2, 63) - 1), pow(2, 63))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            set_Right_most_Unset_Bit('invalid')
