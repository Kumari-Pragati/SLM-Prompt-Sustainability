import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(set_left_most_unset_bit(0b10101010), 0b10101011)
        self.assertEqual(set_left_most_unset_bit(0b11111111), 0b11111111)
        self.assertEqual(set_left_most_unset_bit(0b00000000), 0b00000001)

    def test_edge_cases(self):
        self.assertEqual(set_left_most_unset_bit(0b11111111111111111111111111111111), 0b11111111111111111111111111111111)
        self.assertEqual(set_left_most_unset_bit(0b00000000000000000000000000000000), 0b00000000000000000000000000000001)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(set_left_most_unset_bit(0b11111111111111111111111111111110), 0b11111111111111111111111111111111)
