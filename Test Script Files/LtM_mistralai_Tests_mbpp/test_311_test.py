import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)
        self.assertEqual(set_left_most_unset_bit(3), 4)
        self.assertEqual(set_left_most_unset_bit(7), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(set_left_most_unset_bit(1), 3)
        self.assertEqual(set_left_most_unset_bit(15), 16)
        self.assertEqual(set_left_most_unset_bit(2147483647), 2147483648)
        self.assertEqual(set_left_most_unset_bit(0xFFFFFFFF), 0)

    def test_complex_scenarios(self):
        self.assertEqual(set_left_most_unset_bit(0b1111111111111101), 0b1111111111111110)
        self.assertEqual(set_left_most_unset_bit(0b1010101010101010), 0b1010101010101011)
