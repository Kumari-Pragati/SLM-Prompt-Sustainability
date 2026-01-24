import unittest
from mbpp_671_code import set_Right_most_Unset_Bit

class TestSetRightmostUnsetBit(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(set_Right_most_Unset_Bit(0), 1)
        self.assertEqual(set_Right_most_Unset_Bit(1), 2)
        self.assertEqual(set_Right_most_Unset_Bit(3), 2)
        self.assertEqual(set_Right_most_Unset_Bit(7), 4)

    # Test for edge and boundary conditions
    def test_edge_and_boundary_conditions(self):
        self.assertEqual(set_Right_most_Unset_Bit(8), 8)
        self.assertEqual(set_Right_most_Unset_Bit(15), 8)
        self.assertEqual(set_Right_most_Unset_Bit(255), 128)

    # Test for more complex or corner cases
    def test_more_complex_cases(self):
        self.assertEqual(set_Right_most_Unset_Bit(256), 512)
        self.assertEqual(set_Right_most_Unset_Bit(65535), 32)
        self.assertEqual(set_Right_most_Unset_Bit(67108863), 16)
