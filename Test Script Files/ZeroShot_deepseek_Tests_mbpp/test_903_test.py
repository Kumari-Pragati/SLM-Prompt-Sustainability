import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_count_Unset_Bits(self):
        self.assertEqual(count_Unset_Bits(5), 2)
        self.assertEqual(count_Unset_Bits(10), 4)
        self.assertEqual(count_Unset_Bits(15), 6)
        self.assertEqual(count_Unset_Bits(20), 8)
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(1), 0)
