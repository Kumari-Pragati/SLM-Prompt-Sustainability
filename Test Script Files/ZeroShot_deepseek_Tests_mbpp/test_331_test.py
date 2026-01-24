import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_count_unset_bits(self):
        self.assertEqual(count_unset_bits(0), 0)
        self.assertEqual(count_unset_bits(1), 1)
        self.assertEqual(count_unset_bits(2), 1)
        self.assertEqual(count_unset_bits(3), 0)
        self.assertEqual(count_unset_bits(4), 1)
        self.assertEqual(count_unset_bits(5), 0)
        self.assertEqual(count_unset_bits(6), 2)
        self.assertEqual(count_unset_bits(7), 0)
        self.assertEqual(count_unset_bits(8), 1)
        self.assertEqual(count_unset_bits(9), 0)
        self.assertEqual(count_unset_bits(10), 2)
        self.assertEqual(count_unset_bits(11), 1)
        self.assertEqual(count_unset_bits(12), 2)
        self.assertEqual(count_unset_bits(13), 1)
        self.assertEqual(count_unset_bits(14), 2)
        self.assertEqual(count_unset_bits(15), 0)
        self.assertEqual(count_unset_bits(16), 1)
