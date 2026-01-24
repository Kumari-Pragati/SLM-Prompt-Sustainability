import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(set_left_most_unset_bit(10), 12)
        self.assertEqual(set_left_most_unset_bit(15), 16)
        self.assertEqual(set_left_most_unset_bit(255), 256)
        self.assertEqual(set_left_most_unset_bit(0), 1)

    def test_edge_cases(self):
        self.assertEqual(set_left_most_unset_bit(-1), 0)
        self.assertEqual(set_left_most_unset_bit(1), 2)
        self.assertEqual(set_left_most_unset_bit(2), 3)
        self.assertEqual(set_left_most_unset_bit(256), 513)
        self.assertEqual(set_left_most_unset_bit(511), 512)
        self.assertEqual(set_left_most_unset_bit(1023), 1024)
        self.assertEqual(set_left_most_unset_bit(1025), 1026)

    def test_invalid_input(self):
        self.assertRaises(TypeError, set_left_most_unset_bit, 3.14)
        self.assertRaises(TypeError, set_left_most_unset_bit, "string")
