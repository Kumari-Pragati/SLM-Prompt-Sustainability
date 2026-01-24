import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_left_most_unset_bit(0b1101), 0b1111)
        self.assertEqual(set_left_most_unset_bit(0b1000), 0b1000)
        self.assertEqual(set_left_most_unset_bit(0b1111), 0b1111)

    def test_edge_cases(self):
        self.assertEqual(set_left_most_unset_bit(0), 0b1)
        self.assertEqual(set_left_most_unset_bit(0b11111111), 0b100000000)

    def test_corner_cases(self):
        self.assertEqual(set_left_most_unset_bit(0b11111111111111111111111111111110), 0b11111111111111111111111111111111)
        self.assertEqual(set_left_most_unset_bit(0b11111111111111111111111111111111), 0b11111111111111111111111111111111)
