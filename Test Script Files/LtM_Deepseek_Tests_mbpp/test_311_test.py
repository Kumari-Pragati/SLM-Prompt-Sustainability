import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(set_left_most_unset_bit(0b1101), 0b1111)
        self.assertEqual(set_left_most_unset_bit(0b10101), 0b10111)
        self.assertEqual(set_left_most_unset_bit(0b11111), 0b11111)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(set_left_most_unset_bit(0), 0b1)
        self.assertEqual(set_left_most_unset_bit(0b11111111111111111111111111111111), 0b100000000000000000000000000000000)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(set_left_most_unset_bit(0b1000), 0b1000)
        self.assertEqual(set_left_most_unset_bit(0b11111111111111111111111111111110), 0b11111111111111111111111111111111)
