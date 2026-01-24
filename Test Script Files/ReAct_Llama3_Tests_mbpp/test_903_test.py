import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_Unset_Bits(0), 0)

    def test_one(self):
        self.assertEqual(count_Unset_Bits(1), 0)

    def test_small_positive(self):
        self.assertEqual(count_Unset_Bits(2), 1)

    def test_small_negative(self):
        self.assertEqual(count_Unset_Bits(-2), 1)

    def test_large_positive(self):
        self.assertEqual(count_Unset_Bits(10), 3)

    def test_large_negative(self):
        self.assertEqual(count_Unset_Bits(-10), 3)

    def test_edge_case(self):
        self.assertEqual(count_Unset_Bits(1), 0)

    def test_edge_case_negative(self):
        self.assertEqual(count_Unset_Bits(-1), 0)
