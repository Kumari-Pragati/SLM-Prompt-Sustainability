import unittest
from mbpp_311_code import set_left_most_unset_bit

class TestSetLeftMostUnsetBit(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(set_left_most_unset_bit(10), 12)

    def test_edge_case(self):
        self.assertEqual(set_left_most_unset_bit(0), 1)

    def test_boundary_case(self):
        self.assertEqual(set_left_most_unset_bit(255), 256)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            set_left_most_unset_bit('invalid_input')
