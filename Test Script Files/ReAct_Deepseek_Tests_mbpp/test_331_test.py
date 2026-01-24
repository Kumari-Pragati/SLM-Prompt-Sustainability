import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_unset_bits(0), 32)
        self.assertEqual(count_unset_bits(1), 31)
        self.assertEqual(count_unset_bits(2), 30)
        self.assertEqual(count_unset_bits(4), 28)
        self.assertEqual(count_unset_bits(8), 24)
        self.assertEqual(count_unset_bits(16), 16)
        self.assertEqual(count_unset_bits(32), 0)

    def test_edge_cases(self):
        self.assertEqual(count_unset_bits(2**32 - 1), 0)
        self.assertEqual(count_unset_bits(2**32), 32)
        self.assertEqual(count_unset_bits(2**32 + 1), 31)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(count_unset_bits(-1), 32)
        self.assertEqual(count_unset_bits(-2**32), 32)
        self.assertEqual(count_unset_bits(-2**32 - 1), 31)
