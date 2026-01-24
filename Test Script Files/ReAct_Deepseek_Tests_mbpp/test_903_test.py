import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Unset_Bits(5), 2)
        self.assertEqual(count_Unset_Bits(10), 4)
        self.assertEqual(count_Unset_Bits(15), 6)

    def test_edge_cases(self):
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(1), 0)
        self.assertEqual(count_Unset_Bits(2), 1)
        self.assertEqual(count_Unset_Bits(3), 2)

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any error cases explicitly,
        # we can test for negative inputs and non-integer inputs
        self.assertEqual(count_Unset_Bits(-5), 0)
        self.assertEqual(count_Unset_Bits('five'), 0)
