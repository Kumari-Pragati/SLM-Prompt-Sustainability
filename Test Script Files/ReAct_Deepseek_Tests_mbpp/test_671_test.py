import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0b10100), 0b10110)
        self.assertEqual(set_Right_most_Unset_Bit(0b11000), 0b11001)
        self.assertEqual(set_Right_most_Unset_Bit(0b10000000), 0b10000001)

    def test_edge_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)
        self.assertEqual(set_Right_most_Unset_Bit(0b11111111), 0b100000000)
        self.assertEqual(set_Right_most_Unset_Bit(0b1111111111111111), 0b10000000000000000)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(-1), -1)
        self.assertEqual(set_Right_most_Unset_Bit(0b11111111111111111111111111111110), 0b11111111111111111111111111111111)
