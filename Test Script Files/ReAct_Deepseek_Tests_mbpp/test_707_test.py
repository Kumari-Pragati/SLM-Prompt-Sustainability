import unittest
from mbpp_707_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Set_Bits(0), 0)
        self.assertEqual(count_Set_Bits(1), 1)
        self.assertEqual(count_Set_Bits(2), 1)
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(4), 1)
        self.assertEqual(count_Set_Bits(5), 2)
        self.assertEqual(count_Set_Bits(6), 2)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(8), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Set_Bits(1023), 5)
        self.assertEqual(count_Set_Bits(1024), 1)
        self.assertEqual(count_Set_Bits(2047), 11)
        self.assertEqual(count_Set_Bits(2048), 1)
        self.assertEqual(count_Set_Bits(32767), 19)
        self.assertEqual(count_Set_Bits(32768), 1)

    def test_explicitly_handled_error_cases(self):
        # The function does not handle any explicit error cases, so this test is just to ensure it doesn't crash
        self.assertIsNone(count_Set_Bits(-1))
        self.assertIsNone(count_Set_Bits('abc'))
        self.assertIsNone(count_Set_Bits(None))
