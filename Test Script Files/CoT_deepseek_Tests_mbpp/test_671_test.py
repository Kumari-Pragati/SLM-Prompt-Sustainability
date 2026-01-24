import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)
        self.assertEqual(set_Right_most_Unset_Bit(1), 2)
        self.assertEqual(set_Right_most_Unset_Bit(3), 2)
        self.assertEqual(set_Right_most_Unset_Bit(7), 8)
        self.assertEqual(set_Right_most_Unset_Bit(15), 8)

    def test_edge_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(1023), 1024)
        self.assertEqual(set_Right_most_Unset_Bit(2047), 2048)
        self.assertEqual(set_Right_most_Unset_Bit(4095), 4096)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            set_Right_most_Unset_Bit('invalid')
        with self.assertRaises(TypeError):
            set_Right_most_Unset_Bit(None)
        with self.assertRaises(TypeError):
            set_Right_most_Unset_Bit(1.5)
