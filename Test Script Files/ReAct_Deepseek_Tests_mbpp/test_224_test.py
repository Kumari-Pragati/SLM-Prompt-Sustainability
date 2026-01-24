import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(8), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(2147483647), 31)

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any explicit error cases,
        # we can test with a negative number to ensure it doesn't crash.
        self.assertEqual(count_Set_Bits(-1), 32)
